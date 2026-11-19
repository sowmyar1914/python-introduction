"""Functional Data Processor - beginner-friendly Python practice."""

from functools import reduce
from pprint import pprint

# Original product data. We will not change this list or its dictionaries.
products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]

# 1. filter() keeps only products that are in stock.
in_stock_products = list(filter(lambda product: product["in_stock"], products))

# 2. map() creates NEW dictionaries with a 10% discounted price.
# ** copies each dictionary's fields, so the original is unchanged.
discounted_products = list(
    map(
        lambda product: {
            **product,
            "discounted_price": round(product["price"] * 0.90, 2),
        },
        products,
    )
)

# 3. filter() checks both the category and the price.
affordable_electronics = list(
    filter(
        lambda product: product["category"] == "electronics" and product["price"] < 200,
        products,
    )
)

# 4. sorted() returns a NEW list, from cheapest to most expensive.
sorted_products = sorted(products, key=lambda product: product["price"])

# 5. sum() adds the prices of all in-stock products.
total_in_stock = sum(product["price"] for product in in_stock_products)

# 6. A dictionary comprehension makes one entry for each category.
# For each category, a list comprehension collects matching products.
grouped_by_category = {
    category: [product for product in products if product["category"] == category]
    for category in dict.fromkeys(product["category"] for product in products)
}

# Print all six results in a readable format.
print("1. IN-STOCK PRODUCTS")
pprint(in_stock_products, sort_dicts=False)

print("\n2. ALL PRODUCTS WITH 10% DISCOUNT")
pprint(discounted_products, sort_dicts=False)

print("\n3. ELECTRONICS UNDER $200")
pprint(affordable_electronics, sort_dicts=False)

print("\n4. PRODUCTS SORTED BY PRICE (LOWEST FIRST)")
pprint(sorted_products, sort_dicts=False)

print("\n5. TOTAL VALUE OF IN-STOCK PRODUCTS")
print(f"${total_in_stock:.2f}")

print("\n6. PRODUCTS GROUPED BY CATEGORY")
pprint(grouped_by_category, sort_dicts=False)
