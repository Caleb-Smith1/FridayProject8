import sqlite3

# Connect to (or create) a database file named customer_info.db
conn = sqlite3.connect("customer_info.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create the 'customers' table if it doesn't already exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthday TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        contact_method TEXT NOT NULL
    )
""")

# Save changes and close the connection
conn.commit()
conn.close()

print("✅ Database and table created successfully.")