# Task 4: Data Quality Checks
# Project: Sales Data Exploratory Data Analysis

from pathlib import Path
import pandas as pd


# 1. Define dataset path
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "Superstore.csv"


# 2. Load original dataset
def load_dataset(file_path):
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    return pd.read_csv(file_path, encoding="latin1")


def main():
    try:
        df = load_dataset(DATA_FILE)

        print("=" * 60)
        print("TASK 4: DATA QUALITY CHECKS")
        print("=" * 60)

        # Check 1: Missing values
        print("\n1. MISSING VALUES")
        missing_count = df.isnull().sum()
        missing_percent = (
            df.isnull().mean() * 100
        ).round(2)

        missing_report = pd.DataFrame({
            "Missing_Count": missing_count,
            "Missing_Percentage": missing_percent
        })

        print(missing_report.to_string())

        # Check 2: Duplicate records
        print("\n2. DUPLICATE RECORDS")
        duplicate_count = df.duplicated().sum()
        print(f"Duplicate rows: {duplicate_count}")

        # Check 3: Data types
        print("\n3. DATA TYPES")
        print(df.dtypes.to_string())

        # Check 4: Negative values in relevant columns
        print("\n4. NEGATIVE VALUE CHECKS")

        for column in ["Sales", "Profit", "Quantity", "Discount"]:
            if column in df.columns:
                negative_count = (df[column] < 0).sum()
                print(
                    f"{column}: {negative_count} negative values"
                )

        # Check 5: Discount range
        print("\n5. DISCOUNT RANGE CHECK")

        if "Discount" in df.columns:
            invalid_discount = (
                (df["Discount"] < 0) |
                (df["Discount"] > 1)
            ).sum()

            print(
                f"Discounts outside 0 to 1: {invalid_discount}"
            )
        else:
            print("Discount column not found.")

        # Final summary
        print("\n6. DATA QUALITY SUMMARY")
        print(f"Total rows checked: {len(df)}")
        print(f"Total columns checked: {len(df.columns)}")
        print(
            "Columns containing missing values: "
            f"{(missing_count > 0).sum()}"
        )
        print(f"Duplicate rows found: {duplicate_count}")

        print("\nTask 4 completed successfully!")

    except (FileNotFoundError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()