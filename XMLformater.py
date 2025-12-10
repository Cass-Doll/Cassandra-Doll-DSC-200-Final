import pandas as pd

# Path to the XML file
input_file = "data/_hpi_download_monthly_hpi_master.xml"  # replace with your XML file path
output_file = "output.csv"  # desired output CSV file

# Read XML into a DataFrame
df = pd.read_xml(input_file)

# Save to CSV
df.to_csv(output_file, index=False)

print(f"Converted XML to CSV saved as {output_file}")

input_file = "output.csv"  # Replace with your CSV file path
df = pd.read_csv(input_file)

# Keep only rows where 'place_name' contains "Milwaukee-Waukesha, WI"
df_filtered = df[df['place_name'].str.contains("Milwaukee-Waukesha, WI", na=False)]

# Save the filtered result to a new CSV
filtered_output_file = "filtered_output.csv"
df_filtered.to_csv(filtered_output_file, index=False)


print(f"Filtered CSV saved to {filtered_output_file}")
