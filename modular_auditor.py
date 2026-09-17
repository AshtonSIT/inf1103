#initialise inventory state
from webbrowser import get

#get valid input function
def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit'): ").strip()
    if user_input.lower() == 'quit':
        return "quit"
    if not user_input.isdigit():
        print("Error: Invalid entry. Please enter in number form.")
        return None
    return int(user_input)

#process delivery function
def process_delivery(current_total, new_value):
    return current_total + new_value

#calculate tax function
def calculate_tax(amount):
    return amount * 0.10

#generate report function
def generate_report(total_units, failed_attempts):
    print("\n==============================")
    print(" INVENTORY AUDIT REPORT ")
    print("==============================")
    print("Total Units Processed:", total_units)
    print("Total Failed Attempts:", failed_attempts)



#create main application loop
def main():
    inventory = 0
    errors = 0

    print("Inventory Auditor Report")
    while True:
        #prompt user for input and process it
        result = get_valid_input()
        if result == "quit":
            break
        if result is None:
            errors += 1
            continue

        #process tax calculation and inventory update
        quantity = result
        tax = calculate_tax(quantity)
        inventory = process_delivery(inventory, quantity)
        print(f"Added {quantity} units \nDelivery Tax (10%): {tax:.2f} \nTotal Inventory: {inventory}")

        #overstock alert
        if inventory > 500:
            print("\nOVERSTOCK ALERT: Inventory exceeds 500 units!")
            break

    #print summary report
    generate_report(inventory, errors)
    
if __name__ == "__main__":
    main()