import os

def load_inventory(filename="inventory.txt"):

    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            pass
        return []
    
    try:
        with open(filename, 'r') as f:
            orders = [line.strip() for line in f.readlines() if line.strip()]
            return orders
        
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []


def display_current_orders(orders):

    print("\nCurrent Orders:")

    if orders:
        for order in orders:
            print(order)
    else:
        print("No existing orders found.")
    print()


def get_valid_input():

    qty_input = input("Enter Stock Quantity (or 'quit'): ").strip()

    if qty_input.lower() == 'quit':
        return "quit"
    
    if not qty_input.isdigit():
        print("Error: Invalid entry. Please enter in number form.")
        return None
    
    return int(qty_input)


def process_delivery(current_total, new_value):
    return current_total + new_value


def main():

    orders = load_inventory("inventory.txt")

    history = []
    total_inventory = 0
    for line in orders:
        parts = line.split(',')
        if len(parts) >= 3 and parts[2].strip().isdigit():
            qty = int(parts[2].strip())
            history.append(qty)
            total_inventory += qty

    failed_attempts = 0

    print("--- Persistent Inventory Auditor ---") 
    display_current_orders(orders)

    while True:
        product_name = input("Enter Product Name (or 'quit'): ").strip()
        if product_name.lower() == 'quit':
            break

        qty_result = get_valid_input()

        if qty_result == "quit":
            break

        if qty_result is None:
            failed_attempts += 1
            print()
            continue

        quantity = qty_result
        total_inventory = process_delivery(total_inventory, quantity)
        history.append(quantity)

        print(f"Total Inventory: {total_inventory} | History: {history}")

if __name__ == "__main__":
    main()