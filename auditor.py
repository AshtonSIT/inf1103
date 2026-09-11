#initialise inventory state
inventory = 0
errors = 0

#run continuous loop
while True:
    user_input = input("Enter stock quantity (or 'quit'): ").strip()
    if user_input.lower() == 'quit':
        break

    #handle invalid input
    if not user_input.isdigit():
        print("Error: Invalid entry. Please enter in number form.")
        errors += 1
        continue

    #update running inventory state
    amount = int(user_input)
    inventory += amount
    print(f"Current Inventory: {inventory}")

    #trigger overstock alert
    if inventory > 500:
        print("\nOVERSTOCK ALERT: Inventory exceeds 500 units!")
        break

#reporting
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", errors)