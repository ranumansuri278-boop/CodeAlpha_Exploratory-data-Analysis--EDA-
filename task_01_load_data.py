# Task 2: Load the Superstore Dataset

from pathlib import Path
import pandas as pd


# 1. Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent

# 2. Set the CSV file location
DATA_FILE = PROJECT_DIR / "data" / "raw" / "Superstore.csv"


# 3. Load the dataset
def load_dataset(file_path):

    if not file_path.exists():
        raise FileNotFoundError(
            f"CSV file not found: {file_path}"
        )

    try:
        df = pd.read_csv(file_path, encoding="utf-8-sig")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding="latin-1")

    if df.empty:
        raise ValueError("The CSV file has no data rows.")

    return df


# 4. Run the program
def main():
    try:
        df = load_dataset(DATA_FILE)

        print("=" * 50)
        print("SUPERSTORE DATASET LOADED SUCCESSFULLY")
        print("=" * 50)

        print(f"\nDataset path: {DATA_FILE}")
        print(f"Total rows: {df.shape[0]}")
        print(f"Total columns: {df.shape[1]}")

        print("\nColumn names:")
        print(df.columns.tolist())

        print("\nFirst 5 records:")
        print(df.head().to_string(index=False))

        print("\nTask 2 completed successfully!")

    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()