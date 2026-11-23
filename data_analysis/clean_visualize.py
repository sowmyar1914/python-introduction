from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # Save charts without opening a window.
import matplotlib.pyplot as plt
import pandas as pd


def main():
    messy = pd.DataFrame({
        "product": ["Widget A", "Widget B", "widget a", "Widget C", "Widget B",
                    "Widget A", " Widget C", "Widget D", None, "Widget A"],
        "sales": ["150", "200", "175", "300", "200",
                  "180", "250", "abc", "100", "-50"],
        "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02",
                 "2025-01-03", "2025-01-03", "2025-01-04", "2025-01-04",
                 "2025-01-05", "2025-01-05"],
        "region": ["North", "South", "north", "East", "South",
                   "West", "east", "North", "South", "West"],
    })

    clean = messy.copy()
    for column in ["product", "region"]:
        clean[column] = clean[column].str.strip().str.title().replace("", pd.NA)
    clean["sales"] = pd.to_numeric(clean["sales"], errors="coerce")
    clean["date"] = pd.to_datetime(clean["date"], format="%Y-%m-%d", errors="coerce")

    # This exercise treats negative sales as invalid.
    clean = clean.dropna(subset=["product", "sales", "date", "region"])
    clean = clean.loc[clean["sales"] >= 0]
    invalid_count = len(messy) - len(clean)

    # Compare all four columns so sales on different dates stay separate.
    before_deduplication = len(clean)
    clean = clean.drop_duplicates()
    duplicate_count = before_deduplication - len(clean)

    product_totals = clean.groupby("product")["sales"].sum().sort_values(ascending=False)
    daily_totals = clean.groupby("date")["sales"].sum()

    print(f"Starting rows: {len(messy)}")
    print(f"Rows removed for missing or invalid values: {invalid_count}")
    print(f"Duplicate rows removed: {duplicate_count}")
    print(f"Clean rows: {len(clean)}")
    print(f"Total sales: {clean['sales'].sum():,.0f}")
    print("\nTotal sales by product")
    print(product_totals.to_string())
    print("\nDaily sales totals")
    print(daily_totals.to_string())

    fig, axes = plt.subplots(1, 3, figsize=(13, 4), layout="constrained")

    axes[0].bar(product_totals.index, product_totals.values, color="steelblue")
    axes[0].set(title="Total sales by product", xlabel="Product", ylabel="Total sales")

    axes[1].plot(daily_totals.index, daily_totals.values, marker="o", color="teal")
    axes[1].set(title="Daily sales trend", xlabel="Date", ylabel="Total sales")
    axes[1].set_xticks(daily_totals.index)
    axes[1].set_xticklabels(daily_totals.index.strftime("%b %d"), rotation=30)

    axes[2].hist(clean["sales"], bins=5, color="slateblue", edgecolor="white")
    axes[2].set(title="Sales distribution", xlabel="Sales per record", ylabel="Record count")

    output_dir = Path(__file__).resolve().parent / "output"
    output_dir.mkdir(exist_ok=True)
    chart_path = output_dir / "sales_visualizations.png"
    fig.savefig(chart_path, dpi=180)
    plt.close(fig)
    print(f"\nCharts saved to {chart_path}")


if __name__ == "__main__":
    main()
