USE DATABASE FINANCIAL_DB;
USE SCHEMA ANALYTICS;

CREATE OR REPLACE TABLE stock_prices (
    date DATE,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    open FLOAT,
    volume FLOAT,
    daily_return_pct FLOAT,
    moving_avg_7 FLOAT
);