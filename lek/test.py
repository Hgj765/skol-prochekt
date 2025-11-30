import sqlite3

# 1. Connect to a database (creates one if it doesn’t exist)
conn = sqlite3.connect("example.db")

# 2. Create a cursor object to run SQL commands
cursor = conn.cursor()

# 3. Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,age INTEGER)")

# 4. Commit the changes and close the connection
conn.commit()
conn.close()

print("✅ Table created successfully!")

