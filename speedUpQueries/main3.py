import sqlite3

conn = sqlite3.connect("customer_db.db")
c = conn.cursor()

c.execute("CREATE INDEX email_index on customers (email);")

c.close()
conn.close()
