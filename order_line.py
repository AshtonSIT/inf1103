from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product: Product = product
        self.quantity: int = int(quantity)

    def calculate_subtotal(self) -> float:
        #Returns product price multiplied by quantity for the order line
        return self.product.get_price() * self.quantity

    def display_line(self) -> None:
        print(
            f"Item: {self.product.get_name()} | "
            f"Quantity: {self.quantity} | "
            f"Unit Price: ${self.product.get_price():.2f} | "
            f"Subtotal: ${self.calculate_subtotal():.2f}"
        )