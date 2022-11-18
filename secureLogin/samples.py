import sqlite3
import hashlib

conn = sqlite3.connect('userdata.db')
curr = conn.cursor()

curr.execute(
    """
    CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    )
    """
)

username1, password1 = "mike213", hashlib.sha256("mikepassword".encode()).hexdigest()
print(password1)