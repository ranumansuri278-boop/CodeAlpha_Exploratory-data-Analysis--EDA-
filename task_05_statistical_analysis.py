# Task 6: Statistical Analysis
# Project: Sales Data Exploratory Data Analysis

from pathlib import Path
import pandas as pd


# 1. Define project paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "Superstore.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"


# 2. Load dataset
def load_dataset(file_path):
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    return pd.read_csv(file_path, encoding="latin1")


# 3. Analyze numerical columns
def numerical_analysis(df):
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    summary = df[numeric_columns].describe().T
    summary["median"] = df[numeric_columns].median()
    summary["missing_values"] = df[numeric_columns].isnull().sum()

    return summary


# 4. Group sales and profit by a category
def grouped_analysis(df, group_column):
    required_columns = [group_column, "Sales", "Profit"]

    if not all(column in df.columns for column in required_columns):
        print(f"Skipping {group_column}: required columns not found.")
        return None

    summary = (
        df.groupby(group_column, dropna=False)
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Average_Sales=("Sales", "mean"),
            Order_Records=("Sales", "count")
        )
        .sort_values("Total_Sales", ascending=False)
    )

    return summary


# 5. Run analysis
def main():
    try:
        df = load_dataset(DATA_FILE)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        print("=" * 60)
        print("TASK 6: STATISTICAL ANALYSIS")
        print("=" * 60)

        # Numerical summary
        print("\n1. NUMERICAL STATISTICS")
        stats = numerical_analysis(df)
        print(stats.round(2).to_string())

        stats.to_csv(OUTPUT_DIR / "numerical_summary.csv")

        # Category analysis
        for column in ["Category", "Region", "Sub-Category"]:
            print(f"\n2. SALES AND PROFIT BY {column.upper()}")

            summary = grouped_analysis(df, column)

            if summary is not None:
                print(summary.round(2).to_string())
                summary.to_csv(
                    OUTPUT_DIR / f"{column.lower()}_sales_profit.csv"
                )

        # Overall sales and profit
        print("\n3. OVERALL BUSINESS SUMMARY")

        if "Sales" in df.columns:
            print(f"Total Sales: {df['Sales'].sum():,.2f}")

        if "Profit" in df.columns:
            print(f"Total Profit: {df['Profit'].sum():,.2f}")

        if "Order ID" in df.columns:
            print(f"Unique Orders: {df['Order ID'].nunique():,}")

        print("\nTask 6 completed successfully!")
        print(f"Reports saved in: {OUTPUT_DIR}")

    except (FileNotFoundError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()