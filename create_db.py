import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS scores(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
score INTEGER
)
""")

conn.commit()
conn.close()

print("Database and tables created successfully")