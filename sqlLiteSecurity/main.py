from pysqlcipher3 import dbapi2 as sqlite

conn = sqlite.connect("enc.db")

cur = conn.cursor()

cur.execute("SELECT * FROM people")

print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
