import pandas as pd

#path to the xml
input_file = "data/_hpi_download_monthly_hpi_master.xml"
output_file = "output.csv"

#change from xml to csv
df = pd.read_xml(input_file)
df.to_csv(output_file, index=False)

input_file = "output.csv"
df = pd.read_csv(input_file)

#only rows where place_name is "Milwaukee-Waukesha, WI"
df_filtered = df[df['place_name'].str.contains("Milwaukee-Waukesha, WI", na=False)]

#save to csv
filtered_output_file = "filtered_output.csv"
df_filtered.to_csv(filtered_output_file, index=False)

