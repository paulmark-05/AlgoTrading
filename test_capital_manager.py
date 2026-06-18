from core.capital_manager import (
    CapitalManager
)


print(
    "Capital Per Lot:",
    CapitalManager.capital_per_lot()
)

print(
    "Total Capital:",
    CapitalManager.total_capital()
)

print(
    "Max Lots:",
    CapitalManager.max_lots()
)

print(
    "Capital Required For 3 Lots:",
    CapitalManager.required_capital(3)
)

print(
    "Can Allocate 8 Lots:",
    CapitalManager.can_allocate(8)
)

print(
    "Can Allocate 20 Lots:",
    CapitalManager.can_allocate(20)
)