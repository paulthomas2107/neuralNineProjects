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
username2, password2 = "john", hashlib.sha256("pass123".encode()).hexdigest()
username3, password3 = "striker999", hashlib.sha256("pass456".encode()).hexdigest()
username4, password4 = "neuralnine", hashlib.sha256("really090909".encode()).hexdigest()

curr.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
curr.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
curr.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
curr.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()
