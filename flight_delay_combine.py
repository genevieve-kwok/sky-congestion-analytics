import glob
import sqlite3
import pandas as pd

csv_files = sorted(glob.glob("flight_delays_2025_*.csv"))
df_list = [pd.read_csv(file) for file in csv_files]

combined_df = pd.concat(df_list, ignore_index=True)

with sqlite3.connect("flight_delays.db") as conn:
    combined_df.to_sql("flight_info", conn, if_exists="replace", index=False)
