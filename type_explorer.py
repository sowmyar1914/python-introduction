# type_explorer.py — Understanding Python data types

# Different types look the same when printed
print(42)       # This is an integer
print("42")     # This is a string
print(42.0)     # This is a float
# Numbers support math
print(42 + 8)       # 50

# Strings support concatenation
print("42" + "8")   # "428" (not 50!)
# Use type() to verify what you're working with
value1 = 42
value2 = "42"

print(f"value1 is {type(value1)}")   # <class 'int'>
print(f"value2 is {type(value2)}")   # <class 'str'>
print(f"Are they equal? {value1 == value2}")  # False!
# Product data (often arrives as strings from files or user input)
product_name = "Wireless Mouse"
price_text = "29.99"
quantity_text = "3"
tax_rate_text = "0.08"

# Convert to appropriate types for calculation
price = float(price_text)
quantity = int(quantity_text)
tax_rate = float(tax_rate_text)

# Now we can do math
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# Display results
print(f"Product: {product_name}")
print(f"Price: ${price} x {quantity}")
print(f"Subtotal: ${subtotal:.2f}")    # .2f formats to 2 decimal places
print(f"Tax ({tax_rate * 100}%): ${tax:.2f}")
print(f"Total: ${total:.2f}")