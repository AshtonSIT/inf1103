from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from inventory import Inventory

#Supplier and Products Setup
sup = Supplier("S101", "SATS Engineering", "sats@outlook.com")
laptop = PhysicalProduct("P101", "Gaming Laptop", 1200.0, 10, 2.5, sup)
ebook = DigitalProduct("D201", "Python eBook", 25.0, 100, 15.0, sup)

#Add both distinct product subclasses into the SAME Inventory collection
inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(ebook)

#7.2: Demonstrate Polymorphism (No isinstance() checks)
print("POLYMORPHIC INVENTORY ITERATION")
for product in inventory.products:
    product.display_information()
    print(f"Fulfilment: {product.get_fulfilment_info()}\n")