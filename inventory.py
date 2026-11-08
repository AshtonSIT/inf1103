from product import Product

class Inventory:
    def __init__(self) -> None:
        #Aggregation collection typed with the abstract base class Product
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        #Adds an existing Product object to the inventory list
        self.products.append(product)

    def remove_product(self, product_id: str) -> Product | None:
        #Removes a product from the inventory by its ID and returns the removed product, or None if not found
        for p in self.products:
            if p.get_id() == product_id:
                self.products.remove(p)
                return p
        return None

    def find_product(self, product_id: str) -> Product | None:
        #Finds a product in the inventory by its ID and returns it, or None if not found
        for p in self.products:
            if p.get_id() == product_id:
                return p
        return None

    #Alias for find_product to maintain backward compatibility
    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def display_all(self) -> None:
        #Polymorphically displays all products in the inventory
        if not self.products:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")
        for p in self.products:
            p.display_information()

    def get_all_products(self) -> list[Product]:
        return self.products