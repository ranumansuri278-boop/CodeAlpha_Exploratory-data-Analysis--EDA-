# Task 3: Data Overview
# Project: Sales Data Exploratory Data Analysis

from pathlib import Path
import pandas as pd


# 1. Define project and dataset paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "Superstore.csv"


# 2. Load the dataset
def load_dataset(file_path):
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    return pd.read_csv(file_path, encoding="latin1")


# 3. Display the dataset overview
def main():
    try:
        df = load_dataset(DATA_FILE)

        print("=" * 60)
        print("TASK 3: DATASET OVERVIEW")
        print("=" * 60)

        # Dataset dimensions
        print("\n1. DATASET SIZE")
        print(f"Total rows: {df.shape[0]}")
        print(f"Total columns: {df.shape[1]}")

        # Column names
        print("\n2. COLUMN NAMES")
        for column in df.columns:
            print("-", column)

        # First five records
        print("\n3. FIRST FIVE ROWS")
        print(df.head().to_string(index=False))

        # Data types and non-null counts
        print("\n4. DATA TYPES AND NON-NULL VALUES")
        df.info()

        # Missing values overview
        print("\n5. MISSING VALUES PER COLUMN")
        print(df.isnull().sum().to_string())

        # Descriptive statistics
        print("\n6. NUMERICAL SUMMARY")
        print(df.describe().to_string())

        # Memory usage
        print("\n7. MEMORY USAGE")
        print(f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB")

        print("\nTask 3 completed successfully!")

    except (FileNotFoundError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()