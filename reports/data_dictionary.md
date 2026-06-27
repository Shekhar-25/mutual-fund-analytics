# Data Dictionary

## fact_nav
- amfi_code: Unique fund identifier
- nav_date: Date of NAV
- nav: Net Asset Value

## fact_transactions
- investor_id: Unique investor ID
- transaction_type: SIP / LUMPSUM / REDEMPTION
- amount_inr: Transaction value
- state, city: Geography
- kyc_status: Investor verification status

## fact_performance
- returns: Fund returns
- sharpe_ratio: Risk-adjusted return metric
- expense_ratio: Fund cost percentage