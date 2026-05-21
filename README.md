## Project Overview

End-to-end financial data engineering platform using Python, Snowflake, SQL, Pandas, and Streamlit.

This project is an end-to-end financial data engineering pipeline built using Python, Pandas, Snowflake, and SQL.

The platform extracts stock market data, performs data transformation and cleaning, loads the processed data into Snowflake cloud warehouse, and performs analytical SQL queries for business insights.


---

## Tech Stack

- Python
- Pandas
- Snowflake
- SQL
- yFinance API
- Streamlit (planned)

---

## Project Architecture

Yahoo Finance API
↓
Python Extraction Layer
↓
Pandas Transformation Layer
↓
CSV Storage
↓
Snowflake Stage
↓
Snowflake Warehouse
↓
SQL Analytics Layer

---

## Project Structure

financial-data-platform/

├── data/
│ ├── reliance_stock_data.csv
│ └── reliance_stock_transformed.csv
│
├── sql/
│ ├── 01_create_table.sql
│ ├── 02_create_stage.sql
│ └── 03_analytics_queries.sql
│
├── src/
│ ├── ingestion/
│ │ └── fetch_stock_data.py
│ │
│ ├── transformation/
│ │ └── transform_stock_data.py
│
├── requirements.txt
│
└── README.md

---

## Features Implemented

- Extracted stock market data using Python
- Cleaned and transformed datasets using Pandas
- Calculated:
  - Daily return percentage
  - 7-day moving average
- Built Snowflake warehouse tables and stages
- Loaded transformed CSV data into Snowflake
- Performed SQL analytics queries on stock data

---

## Sample SQL Analytics

### Top Volume Trading Days

```sql
SELECT
    date,
    close,
    volume
FROM FINANCIAL_DB.ANALYTICS.STOCK_PRICES
ORDER BY volume DESC
LIMIT 10;
```

### Average Closing Price

```sql
SELECT
    ROUND(AVG(close), 2) AS avg_close_price
FROM FINANCIAL_DB.ANALYTICS.STOCK_PRICES;
```

### Lowest Daily Returns

```sql
SELECT
    date,
    daily_return_pct
FROM FINANCIAL_DB.ANALYTICS.STOCK_PRICES
ORDER BY daily_return_pct ASC
LIMIT 5;
```

---

## Future Improvements

- Streamlit dashboard integration
- Real-time stock data ingestion
- Airflow pipeline automation
- Multi-stock analytics
- KPI dashboards and visualization

---

## Author

Sachin Carvalho
