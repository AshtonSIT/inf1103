from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id: str = order_id
        #Collection of OrderLine objects to demonstrate Composition
        self.order_lines: list[OrderLine] = []
        #Strategy is used by the Order, not owned by it (association)
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def add_order_line(self, product: Product, quantity: int) -> None:
        #Creates a new OrderLine object and adds it to the order_lines list
        line = OrderLine(product, quantity)
        self.order_lines.append(line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        #Replaces the discount strategy so it can be changed after the order is created
        self.discount = discount

    def calculate_total(self) -> float:
        #Sums the order line subtotals, then lets the discount strategy adjust the total
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

    def display_order_summary(self) -> None:
        print(f"ORDER SUMMARY - Order ID: {self.order_id}")
        if not self.order_lines:
            print("Order is empty.")
            return

        for line in self.order_lines:
            line.display_line()

        print("\n")
        print(f"Total Order Cost: ${self.calculate_total():.2f}")
        print("\n")