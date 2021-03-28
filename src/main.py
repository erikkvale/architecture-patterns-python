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
        self.available_quantity = quantity
        self.eta = eta

    def __len__(self):
        return self.available_quantity

    def allocate(self, order_line: OrderLine):
        self.available_quantity -= order_line.quantity
        


