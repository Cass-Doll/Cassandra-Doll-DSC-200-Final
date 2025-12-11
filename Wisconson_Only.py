import pandas as pd


input_file = "data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
output_file = "Wisconsin_Only.csv"

#dataset
df = pd.read_csv(input_file)

#only rows where StateName is WI
df_WI = df[df["StateName"] == "WI"]

#save result
df_WI.to_csv(output_file, index=False)
