import csv

from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  #Skip the header row
            for row in reader:
                try:
                    product_type, product_id, name, price, stock_quantity = row
                    product = ProductFactory.create(
                        product_type, product_id, name, float(price), int(stock_quantity), supplier
                    )
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as e:
                    print(f"Skipped line {reader.line_num}: {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")