from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        #Collection of OrderLine objects to demonstrate Composition
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        #Creates a new OrderLine object and adds it to the order_lines list
        line = OrderLine(product, quantity)
        self.order_lines.append(line)

    def calculate_total(self) -> float:
        #Calculates the total cost of the order by summing the subtotals of all order lines
        return sum(line.calculate_subtotal() for line in self.order_lines)

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