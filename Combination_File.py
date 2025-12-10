import pandas as pd

# Paths to the CSV files
csv1 = "Flip_and_Remove.csv"
csv2 = "filtered_output.csv"
csv3 = "Wisconsin_Only.csv"

# Read the CSVs normally (keep headers)
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)
df3 = pd.read_csv(csv3)

# Reset indices to ensure they align from the top row
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)
df3.reset_index(drop=True, inplace=True)

# Combine side-by-side
combined_df = pd.concat([df1, df2, df3], axis=1)

# Save result
output_file = "combined.csv"
combined_df.to_csv(output_file, index=False)

print(f"Combined CSV saved as {output_file}")