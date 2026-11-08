from supplier import Supplier
from product import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory

#Polymorphic test function expecting a base Product reference
def show_product_details(product: Product) -> None:
    #Works for ANY product type derived from Product without isinstance() checks
    product.display_information()
    print(f"Fulfilment: {product.get_fulfilment_info()}\n")

#Supplier and Products Setup
sup = Supplier("S101", "SATS Engineering", "sats@outlook.com")
laptop = PhysicalProduct("P101", "Gaming Laptop", 1200.0, 10, 2.5, sup)
ebook = DigitalProduct("D201", "Python eBook", 25.0, 100, 15.0, sup)

print("Testing LSP Substitutability")
show_product_details(laptop)
show_product_details(ebook)

#Verify Inventory can manage both via base Product operations
inv = Inventory()
inv.add_product(laptop)
inv.add_product(ebook)

print("\nInventory Display All (Base Product Abstraction)")
inv.display_all()