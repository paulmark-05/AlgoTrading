from core.allocation_manager import (
AllocationManager
)

print(

    AllocationManager.allocate(
        "Bazooka",
        2
    )

)

print(

    AllocationManager.allocate(
        "TrendRider",
        3
    )

)

print(

    AllocationManager.allocations()
)
