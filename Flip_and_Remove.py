import pandas as pd

#read the csv
input_file = "data/ACSDP1Y2024.DP05-Data.csv"
df = pd.read_csv(input_file)

#transpose the dataframe
df_transposed = df.T
df_transposed.reset_index(inplace=True, drop=True)

#remove rows with "Margin of Error!!"
df_transposed = df_transposed[~df_transposed.apply(lambda row: row.astype(str).str.contains("Margin of Error!!").any(), axis=1)]

#remove the last row (empty)
df_transposed = df_transposed.iloc[:-1]

#save to csv
output_file = "Flip_and_Remove.csv"
df_transposed.to_csv(output_file, index=False)
