# Task 7: Data Visualization
# Project: Sales Data Exploratory Data Analysis

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Project paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "Superstore.csv"
CHART_DIR = PROJECT_DIR / "outputs" / "charts"


# 2. Load the dataset
def load_dataset(file_path):
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    return pd.read_csv(file_path, encoding="latin1")


# 3. Save each chart
def save_chart(filename):
    plt.tight_layout()
    plt.savefig(CHART_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Chart saved: {filename}")


# 4. Create visualizations
def main():
    try:
        df = load_dataset(DATA_FILE)
        CHART_DIR.mkdir(parents=True, exist_ok=True)

        sns.set_theme(style="whitegrid")

        print("=" * 55)
        print("TASK 7: DATA VISUALIZATION")
        print("=" * 55)

        # Chart 1: Sales distribution
        if "Sales" in df.columns:
            sales = pd.to_numeric(df["Sales"], errors="coerce").dropna()

            plt.figure(figsize=(9, 5))
            sns.histplot(sales, bins=30, kde=True)
            plt.title("Distribution of Sales")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")
            save_chart("01_sales_distribution.png")

        # Chart 2: Profit distribution
        if "Profit" in df.columns:
            profit = pd.to_numeric(df["Profit"], errors="coerce").dropna()

            plt.figure(figsize=(9, 5))
            sns.histplot(profit, bins=30, kde=True)
            plt.title("Distribution of Profit")
            plt.xlabel("Profit")
            plt.ylabel("Frequency")
            save_chart("02_profit_distribution.png")

        # Chart 3: Sales by category
        if {"Category", "Sales"}.issubset(df.columns):
            category_sales = (
                df.groupby("Category")["Sales"]
                .sum()
                .sort_values(ascending=False)
                .reset_index()
            )

            plt.figure(figsize=(9, 5))
            sns.barplot(
                data=category_sales,
                x="Category",
                y="Sales"
            )
            plt.title("Total Sales by Category")
            plt.xlabel("Category")
            plt.ylabel("Total Sales")
            save_chart("03_sales_by_category.png")

        # Chart 4: Profit by region
        if {"Region", "Profit"}.issubset(df.columns):
            region_profit = (
                df.groupby("Region")["Profit"]
                .sum()
                .sort_values(ascending=False)
                .reset_index()
            )

            plt.figure(figsize=(9, 5))
            sns.barplot(
                data=region_profit,
                x="Region",
                y="Profit"
            )
            plt.title("Total Profit by Region")
            plt.xlabel("Region")
            plt.ylabel("Total Profit")
            save_chart("04_profit_by_region.png")

        # Chart 5: Sales versus profit
        if {"Sales", "Profit"}.issubset(df.columns):
            plt.figure(figsize=(9, 5))
            sns.scatterplot(
                data=df,
                x="Sales",
                y="Profit",
                alpha=0.5
            )
            plt.title("Relationship Between Sales and Profit")
            plt.xlabel("Sales")
            plt.ylabel("Profit")
            save_chart("05_sales_vs_profit.png")

        # Chart 6: Discount versus profit
        if {"Discount", "Profit"}.issubset(df.columns):
            plt.figure(figsize=(9, 5))
            sns.scatterplot(
                data=df,
                x="Discount",
                y="Profit",
                alpha=0.5
            )
            plt.title("Relationship Between Discount and Profit")
            plt.xlabel("Discount")
            plt.ylabel("Profit")
            save_chart("06_discount_vs_profit.png")

        print("\nTask 7 completed successfully!")
        print(f"Charts are saved in: {CHART_DIR}")

    except (FileNotFoundError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()