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
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Inventory saved successfully to '{filename}'.")
    except Exception as e:
        print(f"Error saving inventory: {e}")