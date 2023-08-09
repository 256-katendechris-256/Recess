from tabulate import tabulate

# Initialize an empty list to store the receipt items
receipt_items = []

# Get input from the user
while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break

    quantity = input("Enter quantity: ")
    amount = input("Enter amount: ")

    # Add the item to the receipt_items list as a tuple
    receipt_items.append((item, quantity, amount))

# Print the tabular representation of the receipt using tabulate
table_headers = ["Item", "Quantity", "Amount"]
table = tabulate(receipt_items, headers=table_headers, tablefmt="grid")
print(table)
