from .function_strategy import Order, Customer, LineItem
from decimal import Decimal
from .registration_decorator import promotion, best_promo


@promotion
def free_order(order: Order) -> Decimal:
    """Returns a discount of the total cost of the order"""
    return Decimal(order.total())


def test_free_order_registration():
    ann = Customer("Ann Smith", 1100)

    cart = [
        LineItem("banana", 4, Decimal(".5")),
        LineItem("apple", 10, Decimal("1.5")),
        LineItem("watermelon", 5, Decimal(5)),
    ]

    # Checking best promos available
    ann_best_regular = Order(ann, cart, best_promo)
    print(f"Ann's best price for regular cart is: {ann_best_regular}")
