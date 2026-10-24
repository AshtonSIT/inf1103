from product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product) -> bool:
        if self.search_product(product.getID()):
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        for p in self.__products:
            if p.getID().lower() == product_id.lower():
                return p
        return None

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        if not self.__products:
            print("Inventory is empty.")
        else:
            for p in self.__products:
                p.display_information()
        print("\n")

    def get_all_products(self) -> list[Product]:
        return self.__products