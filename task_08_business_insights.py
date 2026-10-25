# Task 9: Business Insights and Recommendations
# Project: Sales Data Exploratory Data Analysis

from pathlib import Path
import pandas as pd


# 1. Define paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "Superstore.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
INSIGHTS_FILE = OUTPUT_DIR / "business_insights.txt"


# 2. Load dataset
def load_dataset(file_path):
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    return pd.read_csv(file_path, encoding="latin1")


def main():
    try:
        df = load_dataset(DATA_FILE)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        insights = []

        insights.append("SUPERSTORE BUSINESS INSIGHTS REPORT")
        insights.append("=" * 45)
        insights.append(f"Records analyzed: {len(df)}")
        insights.append(f"Columns analyzed: {len(df.columns)}")

        # 1. Overall sales and profit
        if "Sales" in df.columns:
            df["Sales"] = pd.to_numeric(
                df["Sales"], errors="coerce"
            )
            total_sales = df["Sales"].sum()
            insights.append(f"\nTotal Sales: {total_sales:,.2f}")

        if "Profit" in df.columns:
            df["Profit"] = pd.to_numeric(
                df["Profit"], errors="coerce"
            )
            total_profit = df["Profit"].sum()
            insights.append(f"Total Profit: {total_profit:,.2f}")

            if "Sales" in df.columns and total_sales != 0:
                profit_margin = total_profit / total_sales * 100
                insights.append(
                    f"Overall Profit Margin: {profit_margin:.2f}%"
                )

        # 2. Category insights
        if {"Category", "Sales", "Profit"}.issubset(df.columns):
            category_summary = df.groupby("Category").agg(
                Total_Sales=("Sales", "sum"),
                Total_Profit=("Profit", "sum")
            )

            if not category_summary.empty:
                top_sales_category = category_summary[
                    "Total_Sales"
                ].idxmax()

                top_profit_category = category_summary[
                    "Total_Profit"
                ].idxmax()

                insights.append(
                    "\nCategory with highest sales: "
                    f"{top_sales_category}"
                )
                insights.append(
                    "Category with highest total profit: "
                    f"{top_profit_category}"
                )

                insights.append("\nCategory performance:")
                insights.append(category_summary.round(2).to_string())

        # 3. Regional insights
        if {"Region", "Sales", "Profit"}.issubset(df.columns):
            region_summary = df.groupby("Region").agg(
                Total_Sales=("Sales", "sum"),
                Total_Profit=("Profit", "sum")
            )

            if not region_summary.empty:
                top_region = region_summary[
                    "Total_Profit"
                ].idxmax()

                low_region = region_summary[
                    "Total_Profit"
                ].idxmin()

                insights.append(
                    f"\nRegion with highest total profit: {top_region}"
                )
                insights.append(
                    f"Region with lowest total profit: {low_region}"
                )
                insights.append("\nRegional performance:")
                insights.append(region_summary.round(2).to_string())

        # 4. Discount and profit observations
        if {"Discount", "Profit"}.issubset(df.columns):
            df["Discount"] = pd.to_numeric(
                df["Discount"], errors="coerce"
            )

            discount_summary = df.groupby("Discount")["Profit"].mean()

            if len(discount_summary) > 1:
                highest_discount = discount_summary.idxmax()
                lowest_discount = discount_summary.idxmin()

                insights.append(
                    "\nDiscount level with highest average profit: "
                    f"{highest_discount}"
                )
                insights.append(
                    "Discount level with lowest average profit: "
                    f"{lowest_discount}"
                )

                insights.append(
                    "Note: These are descriptive comparisons, "
                    "not proof that discounts cause profit changes."
                )

        # 5. Save report
        report_text = "\n".join(insights)
        INSIGHTS_FILE.write_text(report_text, encoding="latin1")

        print(report_text)
        print(f"\nInsights saved to: {INSIGHTS_FILE}")
        print("\nTask 9 completed successfully!")

    except (FileNotFoundError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()

    