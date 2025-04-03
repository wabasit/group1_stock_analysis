import pandas as pd
import os

def load_and_clean_data(stocks_dir):
    all_data = []
    for file in os.listdir(stocks_dir):
        if file.endswith('.csv'):
            symbol = file.split('.')[0]  # Extract symbol from filename
            df = pd.read_csv(os.path.join(stocks_dir, file))
            df['Symbol'] = symbol

            # Convert 'Date' column to datetime format
            df['Date'] = pd.to_datetime(df['Date'])

            # Set 'Date' as index
            df.set_index('Date', inplace=True)

            # Handle missing values
            df.ffill(inplace=True)

            # Remove outliers
            for col in ['Open', 'High', 'Low', 'Close', 'Adj Close']:
                # Remove outliers using Z-score method (3 std. away from the mean)
                # mean = df[col].mean()
                # std = df[col].std()
                # df = df[(df[col] >= mean - 3 * std) & (df[col] <= mean + 3 * std)]

                # Remove outliers using IQR method
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            all_data.append(df)  # Append the cleaned DataFrame

    # Combine all data into a single DataFrame
    combined_df = pd.concat(all_data)

    # Standadrdize column names
    combined_df.columns = combined_df.columns.str.lower().str.replace(' ', '_')

    return combined_df 

# Example usage
df = load_and_clean_data('data/stocks/')
# df.to_csv('data/cleaned_stocks.csv', index=False)
df.to_parquet('data/cleaned-stocks.parquet', engine='pyarrow', index=False)  # Save as Parquet file
print(df.head()) 
print(df.shape)
