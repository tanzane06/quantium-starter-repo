import pandas as pd

# 1. LOAD DATA
file_names = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

try:
    # Load all CSV files and combine them
    list_of_dfs = [pd.read_csv(file) for file in file_names]
    df = pd.concat(list_of_dfs, ignore_index=True)

    # 2. PROCESS DATA
    # **NEW STEP**: Clean the 'price' column
    # Remove the '$' and convert the column to a numeric type (float)
    df['price'] = df['price'].replace({'\$': ''}, regex=True).astype(float)

    # Filter for Pink Morsel products
    df = df[df['product'].str.contains('Pink Morsel', case=False, na=False)]

    # Calculate the 'sales' column (this will now work correctly)
    df['sales'] = df['quantity'] * df['price']

    # Select the final columns
    formatted_df = df[['sales', 'date', 'region']]

    # 3. SAVE OUTPUT
    # Save the result to a CSV file without the index
    formatted_df.to_csv('formatted_sales.csv', index=False)

    print("File 'formatted_sales.csv' has been created successfully!")
    if formatted_df.empty:
        print("Warning: The output file is empty. No 'Pink Morsel' data was found.")
    else:
        print(f"Processed {len(formatted_df)} rows of data.")

except FileNotFoundError as e:
    print(f"Error: {e}. Please make sure the file names and paths are correct.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")