import pandas as pd

#path to csv files
csv1 = "Flip_and_Remove.csv"
csv2 = "final_output.csv"
csv3 = "Wisconsin_Only.csv"

#read csvs
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)
df3 = pd.read_csv(csv3)

#start from the top row when combining the files
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)
df3.reset_index(drop=True, inplace=True)

#combine side by side
combined_df = pd.concat([df1, df2, df3], axis=1)

#save the result
output_file = "combined.csv"
combined_df.to_csv(output_file, index=False)


print(f"Combined CSV saved as {output_file}")
