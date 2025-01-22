import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date, interval, output_file):

    try:
        
        stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

        if stock_data.empty:
            print("NO data")
            return

        stock_data.to_csv(output_file)
        print(f"Data for {ticker} saved to {output_file}")

    except Exception as e:
        print(f"An error occured: {e}")


ticker = input("Enter the stock ticker (e.g., RELIANCE.NS): ").strip()
start_date = "2023-01-01"  # Replace with the desired start date
end_date = "2024-01-01"  # Replace with the desired end date
interval = input("Enter the interval ('1d', '1wk', '1mo', etc.): ").strip()
output_file = f"{ticker}.csv"  # Output CSV file name


fetch_stock_data(ticker, start_date, end_date, interval, output_file)