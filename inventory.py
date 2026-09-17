# product inventory using nested dictionary
inventory = {"laptop": {"price": 800, "quantity": 10},"mouse": {"price": 20, "quantity": 50},"keyboard": {"price": 30, "quantity": 30},"monitor": {"price": 150, "quantity": 20}}
# writing the main heading 
print("-------------------- Product Inventory -------------------")
# writing the product details 
print("="*60)
print(f"{'Product':<15}{'Price':<15}{'Quantity':<15}{'Value':<15}")
print("="*60)
# iterating through the inventory dictionary to display product details
for product, details in inventory.items():
    price = details["price"]
    quantity = details["quantity"]
    value = price * quantity
    print(f"{product:<15}{price:<15}{quantity:<15}{value:<15}")

print("="*60)
# calculationg total inventory value 
total_value = 0
for details in inventory.values():
    total_value += details["price"] * details["quantity"]
print(f"\nTotal Inventory Value: ${total_value:.2f}")
# writting the code for looking up a product in the inventory
product_lookup = input("\nEnter the product name to look up: ").lower()
product_details = inventory.get(product_lookup)
if product_details:
    price = product_details["price"]
    quantity = product_details["quantity"]
    value = price * quantity
    print(f"\nProduct: {product_lookup.capitalize()}")
    print(f"Price: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Value: ${value:.2f}")
else:
    print(f"\nProduct '{product_lookup}' not found in the inventory.")

#updating the product quantity 
update_product = input("\nEnter the product name to update quantity: ").lower()
product_to_update = inventory.get(update_product)
if product_to_update:
    print(f"Current quantity: {product_to_update['quantity']}")
    new_quantity = int(input(f"Enter the new quantity: "))
    product_to_update["quantity"] = new_quantity
    print(f"{update_product.title()} quantity updated to {new_quantity}.")
    print(f"{update_product.title()} new value: ${product_to_update['price'] * new_quantity:.2f}")
else:
    print("product not found in the inventory.")
#using set tracking low stock products
low_stock = set()
for product, details in inventory.items():
    if details["quantity"] < 10:
        low_stock.add(product)
print("\n" + "-"*30)
print("Low Stock Products:")
print("-"*30)
if low_stock:
    print("products that need restocking:")
    for product in low_stock:
        print(f"- {product.title()}")
else:
    print("All products are sufficiently stocked.")

          
