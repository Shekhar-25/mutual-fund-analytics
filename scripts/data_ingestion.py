import pandas as pd
from pathlib import Path

# ==========================================================
# Project Directories
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

# ==========================================================
# Find all CSV files
# ==========================================================

csv_files = sorted(RAW_DATA_PATH.glob("*.csv"))

print("=" * 70)
print(f"Found {len(csv_files)} CSV files")
print("=" * 70)

# Dictionary to store all DataFrames
datasets = {}

# ==========================================================
# Load each dataset
# ==========================================================

for file in csv_files:

    print(f"\nLoading: {file.name}")

    try:
        df = pd.read_csv(file)

        # Store DataFrame
        datasets[file.stem] = df

        # Basic Information
        print(f"Shape: {df.shape}")

        print("\nColumns:")
        print(list(df.columns))

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        # Missing Values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Duplicate Rows
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        # Memory Usage
        memory = round(df.memory_usage(deep=True).sum() / 1024, 2)

        print(f"\nMemory Usage: {memory} KB")

        print("-" * 70)

    except Exception as e:

        print(f"Error loading {file.name}")
        print(e)

print("\nAll datasets loaded successfully!")

# ==========================================================
# Dataset Summary
# ==========================================================

print("\n" + "=" * 70)
print("DATASET SUMMARY")
print("=" * 70)

summary = []

for name, df in datasets.items():

    summary.append({
        "Dataset": name,
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    })

summary_df = pd.DataFrame(summary)

print(summary_df)

print("\nETL Data Ingestion Completed Successfully.")