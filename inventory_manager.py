import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
data_file = os.path.join(data_dir, "inventory.json")
line = "-" * 32


#---------------------------------------------------------------------------
#Input helpers (stop the program crashing on bad input)

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please try again.")


def get_int(prompt):
    """Keep asking until the user enters a non-negative whole number."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid whole number. Please try again.")


#---------------------------------------------------------------------------
#Data persistence

def load_inventory():
    if os.path.exists(data_file):
        print("inventory.json file found.")
        try:
            with open(data_file, "r") as f:
                inventory = json.load(f)
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, OSError):
            print("Error reading inventory.json. Starting with an empty inventory.")
            return []
    print("inventory.json file not found. Starting with an empty inventory.")
    return []


def save_inventory(inventory):
    os.makedirs(data_dir, exist_ok=True)
    try:
        with open(data_file, "w") as f:
            json.dump(inventory, f, indent=4)
        return True
    except OSError as e:
        print(f"Error saving inventory to inventory.json: {e}")
        return False


#---------------------------------------------------------------------------
#Data manipulation (CRUD)

def display_all(inventory):
    print("\nCurrent Inventory")
    print(line)
    if not inventory:
        print("No products in inventory.")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | "
              f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print(line)


def search_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("Product ID cannot be empty.")
        return
    if search_product(inventory, product_id) is not None:
        print(f"Product {product_id} already exists. Use Update Stock instead.")
        return

    name = input("Product Name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return
    price = get_float("Price: ")
    stock = get_int("Stock Quantity: ")

    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = search_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    product["stock"] = get_int("New Stock Quantity: ")
    print("Stock updated successfully!")


def search_menu(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip().upper()
    product = search_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print(line)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print(line)


#---------------------------------------------------------------------------
#Menu system

def print_menu():
    print("\nInventory Management Menu")
    print(line)
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Update Stock")
    print("4. Search Product by ID")
    print("5. Save Inventory to File")
    print("6. Exit")
    print(line)


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = load_inventory()

    try:
        while True:
            print_menu()
            option = input("Enter option: ").strip()

            if option == "1":
                display_all(inventory)
            elif option == "2":
                add_product(inventory)
            elif option == "3":
                update_stock(inventory)
            elif option == "4":
                search_menu(inventory)
            elif option == "5":
                print("Saving inventory...")
                if save_inventory(inventory):
                    print("Inventory saved successfully to inventory.json.")
            elif option == "6":
                print("Saving inventory before exit...")
                if save_inventory(inventory):
                    print("Inventory saved successfully.")
                print("Thank you for using Inventory Management System.")
                print("Program terminated.")
                break
            else:
                print("Invalid option. Please enter a number from 1 to 6.")
    except (EOFError, KeyboardInterrupt):
        print("\nInput closed. Saving inventory before exit...")
        save_inventory(inventory)
        print("Program terminated.")


if __name__ == "__main__":
    main()