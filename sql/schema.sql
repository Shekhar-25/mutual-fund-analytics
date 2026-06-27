-- =========================
-- DIMENSION TABLE: FUND MASTER
-- =========================
CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    risk_grade TEXT
);

-- =========================
-- FACT TABLE: NAV HISTORY
-- =========================
CREATE TABLE fact_nav (
    amfi_code TEXT,
    nav_date DATE,
    nav REAL,
    daily_return REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- =========================
-- FACT TABLE: TRANSACTIONS
-- =========================
CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT
);

-- =========================
-- FACT TABLE: PERFORMANCE
-- =========================
CREATE TABLE fact_performance (
    amfi_code TEXT,
    returns REAL,
    sharpe_ratio REAL,
    expense_ratio REAL,
    negative_sharpe BOOLEAN
);