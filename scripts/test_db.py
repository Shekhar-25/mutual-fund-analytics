import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("database/bluestock_mf.db")

# Test 1: check NAV table
nav = pd.read_sql("SELECT * FROM fact_nav LIMIT 5", conn)
print("\nFACT_NAV SAMPLE:")
print(nav)

# Test 2: check transactions
tx = pd.read_sql("SELECT * FROM fact_transactions LIMIT 5", conn)
print("\nFACT_TRANSACTIONS SAMPLE:")
print(tx)

# Test 3: check performance
perf = pd.read_sql("SELECT * FROM fact_performance LIMIT 5", conn)
print("\nFACT_PERFORMANCE SAMPLE:")
print(perf)

conn.close()