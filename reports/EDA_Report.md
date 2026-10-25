# Sales Data Exploratory Data Analysis (EDA)

## Project Overview

This project performs Exploratory Data Analysis (EDA) on a
Superstore sales dataset using Python.

The goal is to understand sales performance, profitability,
data quality, and relationships between business variables.

## Objectives

- Explore the dataset structure and data types.
- Identify missing values and duplicate records.
- Detect potential outliers using the IQR method.
- Calculate descriptive statistics.
- Analyze sales and profit by category and region.
- Create meaningful visualizations.
- Investigate business hypotheses.
- Generate data-driven business insights.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Git and GitHub

## Project Structure

```text
Sales_EDA_Project/
├── data/
│   └── raw/
│       └── Superstore.csv
├── outputs/
│   └── charts/
├── reports/
│   └── EDA_Report.md
├── task_01_load_data.py
├── task_02_data_overview.py
├── task_03_data_quality.py
├── task_04_outlier_analysis.py
├── task_05_statistical_analysis.py
├── task_06_visualizations.py
├── task_07_hypothesis_testing.py
├── task_08_business_insights.py
├── requirements.txt
└── README.md
```

## Installation

1. Install Python 3.
2. Open a terminal in the project directory.
3. Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Run each task from the project root directory:

```bash
python task_01_load_data.py
python task_02_data_overview.py
python task_03_data_quality.py
python task_04_outlier_analysis.py
python task_05_statistical_analysis.py
python task_06_visualizations.py
python task_07_hypothesis_testing.py
python task_08_business_insights.py
```

## Visualizations

The project creates charts to explore:

- Sales distribution
- Profit distribution
- Sales by category
- Profit by region
- Sales versus profit
- Discount versus profit

Charts are saved in `outputs/charts/`.

## Key Findings

Add the verified findings from the generated analysis outputs
and the EDA report here.

Do not add conclusions until the actual results have been checked.

## Business Recommendations

Recommendations will be based on the observed sales and profit
patterns, category and regional performance, and data quality
findings.

## Limitations

- Results depend on the quality and coverage of the dataset.
- Outliers are not necessarily data errors.
- Correlation does not prove causation.
- Statistical test assumptions must be evaluated.
- Findings should be interpreted in the business context.

## Detailed Report

See [EDA_Report.md](reports/EDA_Report.md) for the detailed
analysis, methodology, findings, and conclusions.

## Author

**Ranu**

Data Analytics Portfolio Project