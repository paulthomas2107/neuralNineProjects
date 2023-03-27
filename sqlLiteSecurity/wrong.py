import sqlite3

conn = sqlite3.connect("enc.db")

cur = conn.cursor()

cur.execute("SELECT * FROM people")

print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
