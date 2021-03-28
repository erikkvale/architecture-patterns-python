from datetime import date, timedelta
from src.main import Batch, OrderLine


def test_allocating_to_a_batch_reduces_the_available_quantity():
    """
    Terminology:
        Product -> has -> SKU
        Customers -> place -> orders
        C
    """
    batch = Batch("batch-001", "SMALL-TABLE", quantity=20, eta=date.today())
    order_line = OrderLine('order-ref', "SMALL-TABLE", 2)
    batch.allocate(order_line)
    assert len(batch) == 18