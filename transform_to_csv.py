import sqlite3
import pandas as pd

conn = sqlite3.connect('flight_delays.db')

chunk_size = 100000
first_chunk = True

print("Converting database table to CSV in chunks...")

for chunk in pd.read_sql_query("SELECT * FROM flight_info", conn, chunksize=chunk_size):
    mode = 'w' if first_chunk else 'a'
    header = first_chunk
    
    chunk.to_csv('flight_delays_export.csv', index=False, mode=mode, header=header)
    first_chunk = False
    print(f"Processed a chunk... file is growing.")

conn.close()
print("Done! 'flight_delays_export.csv' is ready for Tableau.")