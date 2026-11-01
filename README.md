# Bitcoin Price Monitoring Platform

A Python-based application for retrieving, storing, and visualizing historical Bitcoin (BTC-USD) price data.

## Features

- Retrieve hourly Bitcoin price data using yfinance.
- Filter historical records by time using Pandas.
- Store cryptocurrency prices, timestamps, and classifications in SQLite.
- Apply rule-based price classification using an If-Then condition.
- Visualize historical price trends through a local Streamlit dashboard using Matplotlib.

## Technologies

- Python
- Pandas
- yfinance
- SQLite
- Streamlit
- Matplotlib

## Project Structure

- init_btc_db.py — Initializes the SQLite database.
- get_btc_data.py — Retrieves, processes, and stores historical Bitcoin prices.
- app_btc.py — Displays the data and visualizations through Streamlit.

## How to Run

Install the required Python packages:

pip install yfinance pandas streamlit matplotlib

Initialize the database:

  python init_btc_db.py

Retrieve the historical data:

  python get_btc_data.py

Launch the dashboard:

  streamlit run app_btc.py

## Notes

- The current data collection script targets historical BTC-USD prices for January 8, 2026.
- Price classifications are based on predefined If-Then rules using a threshold of USD 96,000.
-The application runs locally using Streamlit to display historical Bitcoin price data and visualizations.
