import pandas as pd

# Read the CSV file
input_file = "data/ACSDP1Y2024.DP05-Data.csv"  # replace with your CSV file path
df = pd.read_csv(input_file)

# Transpose the DataFrame
df_transposed = df.T

# Reset the index to make it easier to manipulate rows
df_transposed.reset_index(inplace=True, drop=True)

# Remove rows containing "Margin of Error!!" anywhere
df_transposed = df_transposed[~df_transposed.apply(lambda row: row.astype(str).str.contains("Margin of Error!!").any(), axis=1)]

# Remove the last row
df_transposed = df_transposed.iloc[:-1]

# Save the result to a new CSV
output_file = "Flip_and_Remove.csv"  # Replace with desired output file path
df_transposed.to_csv(output_file, index=False)

print(f"Processed CSV saved to {output_file}")