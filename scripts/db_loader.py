import os
import pandas as pd
from sqlalchemy import create_engine

# =========================
# ENSURE DATABASE FOLDER EXISTS
# =========================
os.makedirs("database", exist_ok=True)

# =========================
# CREATE SQLITE ENGINE
# =========================
engine = create_engine("sqlite:///database/bluestock_mf.db")

# =========================
# LOAD CLEANED DATA
# =========================
nav = pd.read_csv("data/processed/clean_nav.csv")
transactions = pd.read_csv("data/processed/clean_transactions.csv")
performance = pd.read_csv("data/processed/clean_performance.csv")

print("Loading data into database...")

# =========================
# WRITE TO SQLITE TABLES
# =========================
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("DATABASE CREATED SUCCESSFULLY ✔")
print("Location: database/bluestock_mf.db")