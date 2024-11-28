import pandas as pd

# Load the data
df = pd.read_csv('extended_file.csv')

# Loop through columns and encode non-integer columns
for column in df.columns:
    if not pd.api.types.is_integer_dtype(df[column]):
        # Factorize the column to encode unique values as integers
        df[column], _ = pd.factorize(df[column])

# Save the transformed DataFrame to a new CSV file
df.to_csv('extended_file_e.csv', index=False)
