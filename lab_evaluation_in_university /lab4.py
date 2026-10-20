# This program updates an inventory dictionary with a product name and quantity, then displays stock statistics.

# Initial inventory dictionary
inventory = {"pen": 40, "book": 12, "eraser": 25}

# Ask the user for a product name and a quantity to receive
product_name = input("Enter product name: ").strip().lower()
quantity_received = int(input("Enter quantity to receive: "))  # Convert quantity with int()

# Distinguish the update case from the new-product case with the in operator
if product_name in inventory:
    inventory[product_name] += quantity_received
else:
    inventory[product_name] = quantity_received

# Calculate statistics
product_count = len(inventory)             # Display product count with len()
total_items = sum(inventory.values())      # Total with sum() over values()[cite: 2]

# Display results using f-strings[cite: 2]
print("\n--- Inventory Summary ---")
print(f"Total number of products: {product_count}")
print(f"Total items in stock: {total_items}")
print("Product details:")
for product, quantity in inventory.items():  # Every pair with a loop over items()[cite: 2]
    print(f"{product}: {quantity}")
