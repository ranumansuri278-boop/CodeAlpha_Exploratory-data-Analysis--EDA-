# Task 5: Outlier Analysis using IQR
# Project: Sales Data Exploratory Data Analysis

from pathlib import Path
import pandas as pd


# 1. Define project paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "Superstore.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"


# 2. Load the dataset
def load_dataset(file_path):
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    return pd.read_csv(file_path, encoding="latin1")


# 3. Detect outliers using the IQR method
def detect_outliers(df, columns):
    results = []

    for column in columns:
        if column not in df.columns:
            print(f"Skipping missing column: {column}")
            continue

        values = pd.to_numeric(df[column], errors="coerce").dropna()

        if values.empty:
            continue

        q1 = values.quantile(0.25)
        q3 = values.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = values[
            (values < lower_bound) |
            (values > upper_bound)
        ]

        results.append({
            "Column": column,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lower_Bound": lower_bound,
            "Upper_Bound": upper_bound,
            "Outlier_Count": len(outliers),
            "Outlier_Percentage": round(
                len(outliers) / len(values) * 100, 2
            )
        })

    return pd.DataFrame(results)


# 4. Run the analysis
def main():
    try:
        df = load_dataset(DATA_FILE)

        columns_to_check = [
            "Sales", "Profit", "Quantity", "Discount"
        ]

        results = detect_outliers(df, columns_to_check)

        print("=" * 60)
        print("TASK 5: OUTLIER ANALYSIS")
        print("=" * 60)

        if results.empty:
            print("No eligible numerical columns were found.")
        else:
            print(results.to_string(index=False))

            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            output_file = OUTPUT_DIR / "outlier_summary.csv"
            results.to_csv(output_file, index=False)

            print(f"\nOutlier report saved to: {output_file}")

        print("\nTask 5 completed successfully!")

    except (FileNotFoundError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()