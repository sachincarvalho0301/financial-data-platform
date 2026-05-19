import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("📈 Financial Data Platform Dashboard")

# Load transformed dataset
df = pd.read_csv("data/reliance_stock_transformed.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# KPI Metrics
avg_close = round(df["close"].mean(), 2)
max_close = round(df["close"].max(), 2)
min_close = round(df["close"].min(), 2)

# Display KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Average Close", avg_close)
col2.metric("Highest Close", max_close)
col3.metric("Lowest Close", min_close)

st.divider()

# Stock Price Trend
st.subheader("Stock Price Trend")

fig_price = px.line(
    df,
    x="date",
    y="close",
    title="Closing Price Over Time"
)

st.plotly_chart(fig_price)

# Moving Average Trend
st.subheader("7-Day Moving Average")

fig_ma = px.line(
    df,
    x="date",
    y="moving_avg_7",
    title="7-Day Moving Average"
)

st.plotly_chart(fig_ma)

# Volume Analysis
st.subheader("Trading Volume")

fig_volume = px.bar(
    df,
    x="date",
    y="volume",
    title="Daily Trading Volume"
)

st.plotly_chart(fig_volume)

# Show Data Table
st.subheader("Transformed Dataset")

st.dataframe(df)