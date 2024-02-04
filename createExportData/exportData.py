import sqlite3
import pandas as pd

conn = sqlite3.connect('person_data.db')

df = pd.read_sql_query('SELECT * FROM person', conn)

df.to_excel('person_table.xlsx', index=False)

conn.close()
