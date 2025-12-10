import pandas as pd


input_file = "data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"     # your input
output_file = "Wisconsin_Only.csv"  # cleaned output

# Load dataset
df = pd.read_csv(input_file)

# Keep only rows where StateName == "WI"
df_WI = df[df["StateName"] == "WI"]

# Save filtered result
df_WI.to_csv(output_file, index=False)

print(f"Saved WI-only dataset as '{output_file}'.")
print("Original rows:", len(df))
print("Rows with StateName == 'WI':", len(df_WI))
