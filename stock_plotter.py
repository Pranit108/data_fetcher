import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt



def fetch_stock_data(ticker, start_date, end_date, interval, output_file):

    try:
        
        stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

        if stock_data.empty:
            print("NO data")
            return
        stock_data.reset_index(inplace=True)

        stock_data.to_csv(output_file)
        print(f"Data for {ticker} saved to {output_file}")

    except Exception as e:
        print(f"An error occured: {e}")


ticker = input("Enter the stock ticker (e.g., RELIANCE.NS): ").strip()
start_date = "2023-01-01"  # Replace with the desired start date
end_date = "2024-01-01"  # Replace with the desired end date
interval = input("Enter the interval ('1d', '1wk', '1mo', etc.): ").strip()
output_file = (f"{ticker}.csv") # Output CSV file name


fetch_stock_data(ticker, start_date, end_date, interval, output_file)



data = pd.read_csv(f"{ticker}.csv", index_col="Date", parse_dates=True)
print(data.head())

# Convert 'Close' column to numeric, forcing errors to NaN (if any non-numeric data exists)
data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
    
    # Drop any rows where 'Close' is NaN
data = data.dropna(subset=['Close'])

#plotting
plt.figure(figsize=(12, 6))
data["Close"].plot()
plt.title(f"{ticker} Price Graph")
plt.xlabel("Date")
plt.ylabel("Price in INR")
plt.grid()
plt.show()