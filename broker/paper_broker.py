"""
paper_broker.py

PaperBroker v2

Responsibilities
----------------
- Accept and validate orders
- Route orders for execution
- Support partial fills
- Generate execution reports
- Maintain portfolio state
- Maintain trade history
- Maintain order history
- Future-ready for limit/stop order processing
"""

from __future__ import annotations

from decimal import Decimal
from typing import Dict
from uuid import uuid4

from broker.enums import OrderSide
from broker.order import Order
from broker.order_book import OrderBook
from broker.portfolio import Portfolio
from broker.trade import Trade
from broker.trade_book import TradeBook
from broker.execution_report import (
    ExecutionReport,
    ExecutionType,
)


class PaperBroker:
    """
    Paper trading broker.

    The broker currently assumes an immediately executable market,
    but the execution pipeline is structured so that limit orders,
    stop orders, exchange simulation and live brokers can later be
    introduced without changing the public API.
    """

    # -------------------------------------------------------------
    # Construction
    # -------------------------------------------------------------

    def __init__(
        self,
        initial_cash: Decimal,
        commission_per_share: Decimal = Decimal("0"),
        minimum_commission: Decimal = Decimal("0"),
    ) -> None:

        self.portfolio = Portfolio(initial_cash)

        self.order_book = OrderBook()

        self.trade_book = TradeBook()

        self.execution_reports: list[ExecutionReport] = []

        #
        # Latest market prices
        #

        self.market_prices: Dict[str, Decimal] = {}

        #
        # Commission model
        #

        self.commission_per_share = Decimal(
            commission_per_share
        )

        self.minimum_commission = Decimal(
            minimum_commission
        )

    # -------------------------------------------------------------
    # Order Validation
    # -------------------------------------------------------------

    def _validate_buy(
        self,
        quantity: Decimal,
        price: Decimal,
    ) -> None:

        estimated_cost = quantity * price

        if estimated_cost > self.portfolio.cash:

            raise ValueError(
                "Insufficient cash for BUY order."
            )

    def _validate_sell(
        self,
        symbol: str,
        quantity: Decimal,
    ) -> None:

        if not self.portfolio.has_position(symbol):

            raise ValueError(
                f"No open position for {symbol}."
            )

        position = self.portfolio.get_position(symbol)

        if quantity > position.quantity:

            raise ValueError(
                "Cannot sell more than current position."
            )

    def _validate_order(
        self,
        order: Order,
        quantity: Decimal,
        price: Decimal,
    ) -> None:

        if order.side == OrderSide.BUY:

            self._validate_buy(
                quantity,
                price,
            )

            return

        if order.side == OrderSide.SELL:

            self._validate_sell(
                order.symbol,
                quantity,
            )

            return

        raise ValueError(
            f"Unsupported order side: {order.side}"
        )

    # -------------------------------------------------------------
    # Commission
    # -------------------------------------------------------------

    def _calculate_commission(
        self,
        quantity: Decimal,
    ) -> Decimal:

        commission = (
            quantity * self.commission_per_share
        )

        if commission < self.minimum_commission:

            commission = self.minimum_commission

        return commission

    # -------------------------------------------------------------
    # Execution Report Helpers
    # -------------------------------------------------------------

    def _create_execution_report(
        self,
        *,
        order: Order,
        execution_type: ExecutionType,
        quantity: Decimal,
        price: Decimal,
        commission: Decimal,
        message: str = "",
    ) -> ExecutionReport:
        """
        Create and store an execution report.
        """

        report = ExecutionReport(
            order_id=order.order_id,
            execution_type=execution_type,
            symbol=order.symbol,
            side=order.side.value,
            quantity=int(quantity),
            price=Decimal(price),
            commission=Decimal(commission),
            notes=message,
        )

        self.execution_reports.append(report)

        return report

    # -------------------------------------------------------------
    # Market Data
    # -------------------------------------------------------------

    def update_market_price(
        self,
        symbol: str,
        price: Decimal,
    ) -> None:

        price = Decimal(price)

        self.market_prices[symbol] = price

        self.portfolio.update_market_price(
            symbol,
            price,
        )

    def get_market_price(
        self,
        symbol: str,
    ) -> Decimal:

        try:

            return self.market_prices[symbol]

        except KeyError:

            raise ValueError(
                f"No market price available for {symbol}"
            )

    # -------------------------------------------------------------
    # Order Submission
    # -------------------------------------------------------------

    def submit_order(
        self,
        order: Order,
        market_price: Decimal | None = None,
    ):
        """
        Submit an order.

        If a market price is supplied the order is immediately
        routed for execution.

        If no price is supplied the order becomes a resting
        order until process_market() is called.
        """

        if market_price is None:

            market_price = self.market_prices.get(
                order.symbol
            )

        if market_price is not None:

            market_price = Decimal(market_price)

            self._validate_order(
                order,
                Decimal(order.remaining_quantity),
                market_price,
            )

        self.order_book.add(order)

        self._create_execution_report(
            order=order,
            execution_type=ExecutionType.FILL,
            quantity=Decimal("0"),
            price=Decimal("0"),
            commission=Decimal("0"),
            message="Order accepted.",
        )

        #
        # Immediate execution path
        #

        if market_price is not None:

            return self._route_order(
                order,
                market_price,
            )

        #
        # Resting order
        #

        return None

    # -------------------------------------------------------------
    # Routing
    # -------------------------------------------------------------

    def _route_order(
        self,
        order: Order,
        market_price: Decimal,
    ):
        """
        Route an order to the execution engine.

        Market orders execute immediately.

        Limit/Stop orders will later be handled here.
        """

        return self._execute_order(
            order,
            market_price,
        )

    # -------------------------------------------------------------
    # Execution Engine
    # -------------------------------------------------------------

    def _execute_order(
        self,
        order: Order,
        execution_price: Decimal,
        quantity: Decimal | None = None,
    ) -> Trade:
        """
        Execute all or part of an order.
        """

        execution_price = Decimal(execution_price)

        if quantity is None:
            quantity = Decimal(order.remaining_quantity)
        else:
            quantity = Decimal(quantity)

        if quantity <= 0:
            raise ValueError(
                "Execution quantity must be positive."
            )

        if quantity > order.remaining_quantity:
            raise ValueError(
                "Execution exceeds remaining order quantity."
            )

        commission = self._calculate_commission(
            quantity,
        )

        order.add_execution(
            quantity=int(quantity),
            price=execution_price,
            commission=commission,
        )

        trade = Trade(
            trade_id=uuid4().hex,
            order_id=order.order_id,
            symbol=order.symbol,
            side=order.side,
            quantity=int(quantity),
            price=execution_price,
            commission=commission,
        )

        self.trade_book.add(
            trade,
        )

        self.portfolio.apply_trade(
            trade,
        )

        if order.is_filled:

            execution_type = ExecutionType.FILL
            message = "Order completely filled."

        else:

            execution_type = ExecutionType.PARTIAL_FILL
            message = "Order partially filled."

        self._create_execution_report(
            order=order,
            execution_type=execution_type,
            quantity=quantity,
            price=execution_price,
            commission=commission,
            message=message,
        )

        return trade

    # -------------------------------------------------------------
    # Market Processing
    # -------------------------------------------------------------

    def process_market(
        self,
        symbol: str,
        market_price: Decimal,
    ) -> list[Trade]:
        """
        Process all active orders for a symbol.

        Current behaviour:
            All active orders execute immediately.

        Future versions will evaluate order type,
        limit prices, stop prices, IOC/FOK, etc.
        """

        market_price = Decimal(market_price)

        self.update_market_price(
            symbol,
            market_price,
        )

        executed: list[Trade] = []

        for order in self.order_book:

            if order.symbol != symbol:
                continue

            if order.is_closed:
                continue

            trade = self._route_order(
                order,
                market_price,
            )

            if trade is not None:
                executed.append(
                    trade,
                )

        return executed

    # -------------------------------------------------------------
    # Order Access
    # -------------------------------------------------------------

    def get_order(
        self,
        order_id: str,
    ) -> Order | None:

        return self.order_book.get(
            order_id,
        )

    def orders(
        self,
    ) -> OrderBook:

        return self.order_book

    def open_orders(
        self,
        symbol: str | None = None,
    ) -> list[Order]:

        orders: list[Order] = []

        for order in self.order_book:

            if order.is_closed:
                continue

            if symbol is not None:

                if order.symbol != symbol:
                    continue

            orders.append(
                order,
            )

        return orders

    def filled_orders(
        self,
        symbol: str | None = None,
    ) -> list[Order]:

        orders: list[Order] = []

        for order in self.order_book:

            if not order.is_filled:
                continue

            if symbol is not None:

                if order.symbol != symbol:
                    continue

            orders.append(
                order,
            )

        return orders

    def cancel_order(
        self,
        order_id: str,
    ) -> None:

        order = self.order_book.get(
            order_id,
        )

        if order is None:

            raise ValueError(
                f"Unknown order: {order_id}"
            )

        if order.is_closed:

            raise ValueError(
                "Order already closed."
            )

        order.cancel()

        self._create_execution_report(
            order=order,
            execution_type=ExecutionType.CANCEL,
            quantity=Decimal("0"),
            price=Decimal("0"),
            commission=Decimal("0"),
            message="Order cancelled.",
        )

    def cancel_all_orders(
        self,
    ) -> None:

        for order in self.open_orders():

            order.cancel()

            self._create_execution_report(
                order=order,
                execution_type=ExecutionType.CANCEL,
                quantity=Decimal("0"),
                price=Decimal("0"),
                commission=Decimal("0"),
                message="Order cancelled.",
            )

    # -------------------------------------------------------------
    # Trades / Executions
    # -------------------------------------------------------------

    def trades(
        self,
    ) -> TradeBook:

        return self.trade_book

    def executions(
        self,
    ) -> list[ExecutionReport]:

        return list(
            self.execution_reports
        )

    def execution_reports_for_order(
        self,
        order_id: str,
    ) -> list[ExecutionReport]:

        return [

            report

            for report in self.execution_reports

            if report.order_id == order_id

        ]

    # -------------------------------------------------------------
    # Positions
    # -------------------------------------------------------------

    def positions(
        self,
    ):

        return self.portfolio.positions

    def get_position(
        self,
        symbol: str,
    ):

        return self.portfolio.get_position(
            symbol,
        )

    def has_position(
        self,
        symbol: str,
    ) -> bool:

        return self.portfolio.has_position(
            symbol,
        )

    # -------------------------------------------------------------
    # Portfolio Views
    # -------------------------------------------------------------

    @property
    def cash(self) -> Decimal:

        return self.portfolio.cash

    @property
    def equity(self) -> Decimal:

        return self.portfolio.equity

    @property
    def market_value(self) -> Decimal:

        return self.portfolio.market_value

    @property
    def realized_pnl(self) -> Decimal:

        return self.portfolio.realized_pnl

    @property
    def unrealized_pnl(self) -> Decimal:

        return self.portfolio.unrealized_pnl

    @property
    def total_pnl(self) -> Decimal:

        return self.portfolio.total_pnl

    # -------------------------------------------------------------
    # Utilities
    # -------------------------------------------------------------

    def reset(
        self,
    ) -> None:
        """
        Reset broker state.
        """

        self.portfolio.reset()

        self.order_book.clear()

        self.trade_book.clear()

        self.execution_reports.clear()

        self.market_prices.clear()

    def __repr__(
        self,
    ) -> str:

        return (
            f"{self.__class__.__name__}("
            f"cash={self.cash}, "
            f"equity={self.equity}, "
            f"orders={len(self.order_book)}, "
            f"trades={len(self.trade_book)})"
        )
