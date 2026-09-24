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
    

def order_id(orders):

    if not orders:
        return 1001
    
    existing_id = []
    for line in orders:
        parts = line.split(',')
        if parts[0].strip().isdigit():
            existing_id.append(int(parts[0].strip()))

    return max(existing_id) + 1 if existing_id else 1001


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


def save_inventory(order_line, filename="inventory.txt"):
    with open(filename, 'a') as f:
        f.write(order_line + '\n')


def generate_report(total_inventory, failed_attempts, history):
    print("\n==============================")
    print(" INVENTORY AUDIT REPORT ")
    print("==============================")
    print("Total Units Processed:", total_inventory)
    print("Total Failed Attempts:", failed_attempts)
    print("Transaction History List: ", history)


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

        next_order_id = order_id(orders)
        order_line = f"{next_order_id},{product_name},{quantity}"

        orders.append(order_line)
        save_inventory(order_line, "inventory.txt")

        print("\nNew Order Added:")
        print(order_line)
        print(f"Total Inventory: {total_inventory}")

        display_current_orders(orders)

        if total_inventory > 500:
            print("OVERSTOCK ALERT: Inventory exceeds 500 units!")
            break

    generate_report(total_inventory, failed_attempts, history)


if __name__ == "__main__":
    main()