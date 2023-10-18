from .function_strategy import (
    Customer,
    LineItem,
    Order,
    fidelity_promo,
    bulk_item_promo,
    large_order_promo,
    best_promo,
)
from decimal import Decimal
from .new_strategy import test_free_order_registration


def main():
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1100)

    cart = [
        LineItem("banana", 4, Decimal(".5")),
        LineItem("apple", 10, Decimal("1.5")),
        LineItem("watermelon", 5, Decimal(5)),
    ]

    order_joe = Order(joe, cart, fidelity_promo)
    print(f"Joe's order: {order_joe}")

    order_ann = Order(ann, cart, fidelity_promo)
    print(f"Ann's order: {order_ann}")

    banana_cart = [
        LineItem("banana", 30, Decimal(".5")),
        LineItem("apple", 10, Decimal("1.5")),
    ]

    order_banana_joe = Order(joe, banana_cart, bulk_item_promo)
    print(f"Joe's banana bulk order: {order_banana_joe}")

    long_cart = [LineItem(str(item_code), 1, Decimal(1)) for item_code in range(10)]
    order_long_ann = Order(ann, long_cart, large_order_promo)
    print(f"Ann's large order: {order_long_ann}")

    # Checking best promos available
    joe_best_long = Order(joe, long_cart, best_promo)
    joe_best_bulk = Order(joe, banana_cart, best_promo)
    ann_best_regular = Order(ann, cart, best_promo)
    print(f"Joe's best price for long cart is: {joe_best_long}")
    print(f"Joe's best price for banana bulk cart is: {joe_best_bulk}")
    print(f"Ann's best price for regular cart is: {ann_best_regular}")

    test_free_order_registration()


if __name__ == "__main__":
    main()
