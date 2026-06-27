"""
Unit tests for broker.order
"""

from decimal import Decimal

from broker.order import Order
from broker.enums import OrderSide, OrderType


def test_market_order():
    print("\nTEST 1 : Market Order")

    order = Order(
        symbol="AAPL",
        side=OrderSide.BUY,
        quantity=100,
        order_type=OrderType.MARKET,
    )

    print(order)
    print("PASS")


def test_limit_order():
    print("\nTEST 2 : Limit Order")

    order = Order(
        symbol="AAPL",
        side=OrderSide.BUY,
        quantity=100,
        order_type=OrderType.LIMIT,
        price=Decimal("180.50"),
    )

    print(order)
    print("PASS")


def test_missing_limit_price():
    print("\nTEST 3 : Missing Limit Price")

    try:
        Order(
            symbol="AAPL",
            side=OrderSide.BUY,
            quantity=100,
            order_type=OrderType.LIMIT,
        )
        print("FAIL (No exception raised)")
    except Exception as e:
        print(type(e).__name__, e)


def test_negative_price():
    print("\nTEST 4 : Negative Price")

    try:
        Order(
            symbol="AAPL",
            side=OrderSide.BUY,
            quantity=100,
            order_type=OrderType.LIMIT,
            price=Decimal("-10"),
        )
        print("FAIL (No exception raised)")
    except Exception as e:
        print(type(e).__name__, e)


def test_zero_quantity():
    print("\nTEST 5 : Zero Quantity")

    try:
        Order(
            symbol="AAPL",
            side=OrderSide.BUY,
            quantity=0,
            order_type=OrderType.MARKET,
        )
        print("FAIL (No exception raised)")
    except Exception as e:
        print(type(e).__name__, e)


def test_empty_symbol():
    print("\nTEST 6 : Empty Symbol")

    try:
        Order(
            symbol="",
            side=OrderSide.BUY,
            quantity=10,
            order_type=OrderType.MARKET,
        )
        print("FAIL (No exception raised)")
    except Exception as e:
        print(type(e).__name__, e)


if __name__ == "__main__":
    print("=" * 60)
    print("ORDER MODULE TESTS")
    print("=" * 60)

    test_market_order()
    test_limit_order()
    test_missing_limit_price()
    test_negative_price()
    test_zero_quantity()
    test_empty_symbol()

    print("\nAll Order tests completed.")