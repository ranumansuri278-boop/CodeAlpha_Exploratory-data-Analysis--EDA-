# Task 8: Hypothesis Testing
# Project: Sales Data Exploratory Data Analysis

from pathlib import Path
import pandas as pd
from scipy.stats import pearsonr, f_oneway


# 1. Define paths
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


def main():
    try:
        df = load_dataset(DATA_FILE)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        results = []

        print("=" * 60)
        print("TASK 8: HYPOTHESIS TESTING")
        print("=" * 60)

        # Test 1: Discount and Profit correlation
        print("\n1. DISCOUNT AND PROFIT RELATIONSHIP")

        if {"Discount", "Profit"}.issubset(df.columns):
            data = df[["Discount", "Profit"]].copy()

            data["Discount"] = pd.to_numeric(
                data["Discount"], errors="coerce"
            )
            data["Profit"] = pd.to_numeric(
                data["Profit"], errors="coerce"
            )
            data = data.dropna()

            if (
                len(data) >= 3
                and data["Discount"].nunique() > 1
                and data["Profit"].nunique() > 1
            ):
                correlation, p_value = pearsonr(
                    data["Discount"], data["Profit"]
                )

                print(f"Records analyzed: {len(data)}")
                print(f"Pearson correlation: {correlation:.4f}")
                print(f"P-value: {p_value:.6f}")

                if p_value < 0.05:
                    print(
                        "Result: Evidence of a linear association "
                        "at the 5% significance level."
                    )
                else:
                    print(
                        "Result: Insufficient evidence of a linear "
                        "association at the 5% significance level."
                    )

                results.append({
                    "Test": "Discount vs Profit",
                    "Method": "Pearson correlation",
                    "Statistic": correlation,
                    "P_Value": p_value,
                    "Records": len(data),
                    "Significant_at_0.05": p_value < 0.05
                })
            else:
                print("Not enough valid variation for this test.")
        else:
            print("Required columns not found.")

        # Test 2: Average profit across product categories
        print("\n2. PROFIT DIFFERENCES ACROSS CATEGORIES")

        if {"Category", "Profit"}.issubset(df.columns):
            data = df[["Category", "Profit"]].copy()
            data["Profit"] = pd.to_numeric(
                data["Profit"], errors="coerce"
            )
            data = data.dropna()

            groups = [
                group["Profit"].to_numpy()
                for _, group in data.groupby("Category")
            ]

            category_names = [
                name for name, _ in data.groupby("Category")
            ]

            if len(groups) >= 2 and all(
                len(group) >= 2 for group in groups
            ):
                f_stat, p_value = f_oneway(*groups)

                print(f"Categories analyzed: {category_names}")
                print(f"ANOVA F-statistic: {f_stat:.4f}")
                print(f"P-value: {p_value:.6f}")

                if p_value < 0.05:
                    print(
                        "Result: Evidence that at least one category "
                        "has a different mean profit."
                    )
                else:
                    print(
                        "Result: Insufficient evidence of different "
                        "mean profits across categories."
                    )

                results.append({
                    "Test": "Profit across categories",
                    "Method": "One-way ANOVA",
                    "Statistic": f_stat,
                    "P_Value": p_value,
                    "Records": len(data),
                    "Significant_at_0.05": p_value < 0.05
                })
            else:
                print("Not enough categories or records for ANOVA.")
        else:
            print("Required columns not found.")

        # Save results
        if results:
            result_df = pd.DataFrame(results)
            output_file = OUTPUT_DIR / "hypothesis_test_results.csv"
            result_df.to_csv(output_file, index=False)
            print(f"\nResults saved to: {output_file}")
        else:
            print("\nNo tests could be completed.")

        print("\nTask 8 completed!")

    except (FileNotFoundError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()