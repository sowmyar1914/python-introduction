print("=" * 40)  # Prints a line of 40 equal signs
print(f"{'STORE RECEIPT':^40}")  # Centered title
print("=" * 40)
item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"   # 7.5% sales tax
# convert string values to appropriate types for calculation
item1_price = float(item1_price)
item1_qty = int(item1_qty)
item2_price = float(item2_price)
item2_qty = int(item2_qty)
item3_price = float(item3_price)
item3_qty = int(item3_qty)
tax_rate = float(tax_rate)
#calculating line totals for each item
item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty
#calculating subtotal, tax, and total
subtotal = item1_total + item2_total + item3_total
tax = subtotal * tax_rate
total = subtotal + tax
# Print the formatted receipt

print(f"{item1_name:<15}${item1_price:<6.2f} x {item1_qty:<5}${item1_total:.2f}")
print(f"{item2_name:<15}${item2_price:<6.2f} x {item2_qty:<5}${item2_total:.2f}")
print(f"{item3_name:<15}${item3_price:<6.2f} x {item3_qty:<5}${item3_total:.2f}")

print("-" * 40)
print(f"{'Subtotal:':<30}${subtotal:.2f}")
print(f"{'Tax (7.5%):':<30}${tax_rate:.2f}")
print("=" * 40)
print(f"{'Total:':<30}${total:.2f}")
print("=" * 40)