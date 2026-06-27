import pandas as pd

# =========================
# LOAD NAV DATA
# =========================
nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Original NAV Shape:", nav.shape)

# CLEAN NAV
nav['date'] = pd.to_datetime(nav['date'], errors='coerce')
nav = nav.drop_duplicates()
nav = nav[nav['nav'].notna()]
nav = nav[nav['nav'] > 0]
nav = nav.sort_values(['amfi_code', 'date'])

# forward fill NAV per fund
nav['nav'] = nav.groupby('amfi_code')['nav'].ffill()

nav.to_csv("data/processed/clean_nav.csv", index=False)

print("NAV CLEANING COMPLETED ✔")


# =========================
# LOAD TRANSACTIONS DATA
# =========================
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

transactions.columns = transactions.columns.str.lower()

print("\nTransaction Columns:", transactions.columns)
print("Original Transactions Shape:", transactions.shape)

# AUTO DETECT AMOUNT COLUMN
amount_col = None
for col in transactions.columns:
    if "amount" in col or "value" in col or "amt" in col:
        amount_col = col
        break

if amount_col is None:
    raise Exception("No amount column found")

print("Detected Amount Column:", amount_col)

# CLEAN TRANSACTIONS (SAFE VERSION)
transactions['transaction_type'] = transactions['transaction_type'].str.upper()

transactions[amount_col] = pd.to_numeric(transactions[amount_col], errors='coerce')

# IMPORTANT FIX:
# only remove NULL values, NOT all positive filtering
transactions = transactions.dropna(subset=[amount_col])

# FIX DATE COLUMN
date_col = None
for col in transactions.columns:
    if "date" in col:
        date_col = col
        break

if date_col:
    transactions[date_col] = pd.to_datetime(transactions[date_col], errors='coerce')

# OPTIONAL: keep KYC BUT DO NOT REMOVE DATA
if 'kyc_status' in transactions.columns:
    transactions['kyc_status'] = transactions['kyc_status'].fillna("UNKNOWN")

transactions = transactions.drop_duplicates()

transactions.to_csv("data/processed/clean_transactions.csv", index=False)

print("TRANSACTIONS CLEANING COMPLETED ✔")


# =========================
# LOAD PERFORMANCE DATA
# =========================
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

performance.columns = performance.columns.str.lower()

print("\nOriginal Performance Shape:", performance.shape)

# SAFE NUMERIC CONVERSION
for col in performance.columns:
    if any(x in col for x in ['return', 'ratio', 'expense', 'sharpe']):
        performance[col] = pd.to_numeric(performance[col], errors='coerce')

# FLAG NEGATIVE SHARPE
if 'sharpe_ratio' in performance.columns:
    performance['negative_sharpe'] = performance['sharpe_ratio'] < 0

# EXPENSE FILTER (SAFE)
if 'expense_ratio' in performance.columns:
    performance = performance[
        performance['expense_ratio'].between(0.1, 2.5)
    ]

performance.to_csv("data/processed/clean_performance.csv", index=False)

print("PERFORMANCE CLEANING COMPLETED ✔")

print("\nALL CLEANING DONE SUCCESSFULLY ✔")