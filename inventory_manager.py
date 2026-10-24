import json
import os

from product import Product
from inventory import Inventory

FILENAME = "inventory.json"

def load_inventory_data(filename=FILENAME) -> Inventory:
    inventory = Inventory()

    if not os.path.exists(filename):
        print(f"No '{filename}' found. Starting with empty inventory.\n")
        return inventory

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            for i in data:
                product = Product(i["id"], i["name"], i["price"], i["stock"])
                inventory.add_product(product)
        print(f"{filename} loaded successfully.\n")
    except Exception as e:
        print(f"Error loading {filename}: {e}\n")

    return inventory


def save_inventory_data(inventory: Inventory, filename=FILENAME) -> None:
    try:
        data = [p.to_dict() for p in inventory.get_all_products()]
        with open(filename, "w") as file
            json.dump(data, file, indent=4)
        print(f"Inventory saved successfully to '{filename}'.")
    except Exception as e:
        print(f"Error saving inventory: {e}")


def main():
    print("\n    OOP Inventory Management System    \n")

    inventory = load_inventory_data()

    while True:
        print("\n    Menu    ")
        print("1. Display All Products")
        print("2. Add a Product")
        print("3. Update Stock")
        print("4. Search for a Product")
        print("5. Save Inventory")
        print("6. Exit\n")

        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            productID = input("Product ID: ").strip()
            if inventory.search_product(productID):
                print("Error: Product ID already exists.")
                continue

            name = input("Product Name: ").strip()
            try:
                price = float(inpt("Price: "))
                stock = int(input("Stock Quantity: "))
                new_product = Product(productID, name, price, stock)
                inventory.add_product(new_product)
                print("\nProduct added successfully.")
            except ValueError:
                print("Error: Invalid price or stock value.")

        elif choice == "3":
            productID = input("Product ID: ").strip()
            product = inventory.search_product(productID)

            if product:
                print(
                    f"\nProduct Found:\n"
                    f"Name: {product.getName()}\n"
                    f"Current Stock: {product.getStock()}\n"
                )
                try:
                    new_stock = int(input("New Stock Quantity: "))
                    product.update_stock(new_stock)
                    print("\nStock updated successfully.")
                except ValueError:
                    print("Error: Invalid number entered.")
            else:
                print("\nProduct not found.")

        elif choice == "4":
            productID = input("Enter Product ID: ").strip()
            product = inventory.search_product(productID)

            if product:
                print("\nProduct Found:")
                product.display_information()
                print("\n")
            else:
                print("\nProduct not found.")

        elif choice == "5":
            save_inventory_data(inventory)

        elif choice == "6":
            save_inventory_data(inventory)
            print("\nProgram terminated.")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()