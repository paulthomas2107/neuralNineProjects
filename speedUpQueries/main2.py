import time
import sqlite3

conn = sqlite3.connect("customer_db.db")
c = conn.cursor()

start = time.perf_counter_ns()

c.execute("SELECT * FROM customers WHERE email = 'joseph78@example.org'")

results = c.fetchall()

end = time.perf_counter_ns()

print(results)
print(end - start, "ns")

c.close()
conn.close()

# 382840
# 304891

