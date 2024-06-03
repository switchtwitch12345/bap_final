import sqlite3

# Establish a connection to the SQLite database
connection = sqlite3.connect("sneaker_details.db")

# Print a message indicating that the database is opened successfully
print("Database opened successfully")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Create a table named sneaker_Info with the appropriate columns
cursor.execute("CREATE TABLE IF NOT EXISTS sneaker_Info (\
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                brand TEXT NOT NULL, \
                model TEXT NOT NULL, \
                size TEXT NOT NULL, \
                gender TEXT NOT NULL, \
                colour TEXT NOT NULL, \
                price TEXT NOT NULL)")

# Print a message indicating that the table is created successfully
print("Table created successfully")

# Close the connection to the database
connection.close()
