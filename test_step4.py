from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from order import Order

#Supplier and Products Setup
sup = Supplier("S101", "SATS Engineering", "sats@outlook.com")
laptop = PhysicalProduct("P101", "Gaming Laptop", 1200.0, 10, 2.5, sup)
ebook = DigitalProduct("D201", "Python eBook", 25.0, 100, 15.0, sup)

#Create Order 1 and add products internally via add_order_line()
order1 = Order("1001")
order1.add_order_line(laptop, 2)
order1.add_order_line(ebook, 1)
order1.display_order_summary()

#Create Order 2 and add the SAME product (laptop)
order2 = Order("1002")
order2.add_order_line(laptop, 1)
order2.display_order_summary()

#Verify Predict First experiment (Object Identity Verification)
line1 = order1.order_lines[0]  # laptop line in Order 1
line2 = order2.order_lines[0]  # laptop line in Order 2

print("\nComposition Object Identity Check")
print(f"OrderLine 1 ID: {id(line1)}")
print(f"OrderLine 2 ID: {id(line2)}")
print(f"Are OrderLines identical objects? {line1 is line2}")  #Expected: False

print(f"\nProduct in OrderLine 1 ID: {id(line1.product)}")
print(f"Product in OrderLine 2 ID: {id(line2.product)}")
print(f"Are underlying Products identical objects? {line1.product is line2.product}")  #Expected: True