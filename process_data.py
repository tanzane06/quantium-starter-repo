import pandas as pd

# 1. LOAD DATA
# Corrected list of file names
file_names = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# If your files are named differently, just update the list above.

try:
    # Load all CSV files into a list of DataFrames
    list_of_dfs = [pd.read_csv(file) for file in file_names]

    # Combine all DataFrames into a single one
    df = pd.concat(list_of_dfs, ignore_index=True)

    # 2. PROCESS DATA
    # This flexible filter will find all Pink Morsel products
    df = df[df['product'].str.contains('Pink Morsel', case=False, na=False)]

    # Create a 'sales' column by multiplying quantity and price
    df['sales'] = df['quantity'] * df['price']

    # Select only the columns needed for the final output
    formatted_df = df[['sales', 'date', 'region']]

    # 3. SAVE OUTPUT
    formatted_df.to_csv('formatted_sales.csv', index=False)

    print("File 'formatted_sales.csv' has been created successfully!")
    if formatted_df.empty:
        print("Warning: The output file is empty. No 'Pink Morsel' data was found.")
    else:
        print(f"Processed {len(formatted_df)} rows of data.")

except FileNotFoundError as e:
    print(f"Error: {e}. Please make sure the file names and paths in the 'file_names' list are correct.")