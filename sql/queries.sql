-- 1. Top NAV records (latest values per fund)
SELECT amfi_code, MAX(nav_date) as latest_date, nav
FROM fact_nav
GROUP BY amfi_code;
-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav) as avg_nav
FROM fact_nav
GROUP BY amfi_code;
-- 3. Monthly NAV trend
SELECT strftime('%Y-%m', nav_date) as month, AVG(nav)
FROM fact_nav
GROUP BY month;
-- 4. Total transaction volume
SELECT SUM(amount_inr) as total_investment
FROM fact_transactions;
-- 5. Transactions by type
SELECT transaction_type, COUNT(*) as count
FROM fact_transactions
GROUP BY transaction_type;
-- 6. State-wise investments
SELECT state, SUM(amount_inr) as total
FROM fact_transactions
GROUP BY state
ORDER BY total DESC;
-- 7. High income investor behavior
SELECT age_group, AVG(amount_inr)
FROM fact_transactions
GROUP BY age_group;
-- 8. KYC status distribution
SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;
-- 9. Negative Sharpe ratio funds
SELECT amfi_code
FROM fact_performance
WHERE negative_sharpe = 1;
-- 10. Expense ratio filter (efficient funds)
SELECT amfi_code, expense_ratio
FROM fact_performance
WHERE expense_ratio < 1;