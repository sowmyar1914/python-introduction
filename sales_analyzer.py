# importing data from sales_data.csv
import csv
from collections import defaultdict

total_revenue = 0
revenue_per_product = defaultdict(float)
quantity_for_product = defaultdict(int)
revenue_per_day = defaultdict(float)

# reading every line in the csv file
with open("sales_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row["date"]
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])

        revenue = quantity * price

        total_revenue += revenue
        revenue_per_product[product] += revenue
        quantity_for_product[product] += quantity
        revenue_per_day[date] += revenue


# calculating highest revenue
highest_revenue_day = max(
    revenue_per_day,
    key=revenue_per_day.get
)


# creating sales report
with open("sales_report.txt", "w") as report:

    report.write("Sales Summary Report\n")
    report.write("=" * 30 + "\n")

    report.write(
        f"Total Revenue: ${total_revenue:.2f}\n\n"
    )

    report.write("Revenue Per Product:\n")

    for product in sorted(revenue_per_product):
        report.write(
            f"{product}: "
            f"${revenue_per_product[product]:.2f}\n"
        )

    report.write(
        "\nTotal Quantity Sold Per Product:\n"
    )

    for product in sorted(quantity_for_product):
        report.write(
            f"{product}: "
            f"{quantity_for_product[product]}\n"
        )

    report.write(
        f"\nDay With Highest Total Revenue: "
        f"{highest_revenue_day} "
        f"(${revenue_per_day[highest_revenue_day]:.2f})\n"
    )


# creating product summary csv
with open(
    "product_summary.csv",
    "w",
    newline=""
) as file:

    fieldnames = [
        "product",
        "total_quantity",
        "total_revenue"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for product in sorted(quantity_for_product):

        writer.writerow({
            "product": product,
            "total_quantity":
                quantity_for_product[product],

            "total_revenue":
                f"{revenue_per_product[product]:.2f}"
        })


print("Analysis complete.")
print(
    "Created sales_report.txt "
    "and product_summary.csv"
)