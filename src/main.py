"""
The main event
"""
from datetime import date, timedelta
from typing import Optional


class OrderLine:

    def __init__(self, order_id: str, sku: str, quantity: int):
        self.order_id = order_id
        self.sku = sku
        self.quantity = quantity



class Batch:

    def __init__(self, reference_id: str, sku: str, quantity: int, eta: Optional[date]):
        self.reference_id = reference_id
        self.sku = sku
        self._purchased_quantity = quantity
        self.eta = eta
        self._allocations = set()

    def __len__(self):
        return self.available_quantity

    def allocate(self, order_line: OrderLine):
        if self.can_allocate(order_line):
            self._allocations.add(order_line)

    def deallocate(self, order_line: OrderLine):
        if order_line in self._allocations:
            self._allocations.remove(order_line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, order_line: OrderLine) -> bool:
        return self.sku == order_line.sku and self.available_quantity >= order_line.quantity