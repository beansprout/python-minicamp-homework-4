import sqlite3

connection = sqlite3.connect('database.db')
# execute database commands
connection.execute('CREATE TABLE IF NOT EXISTS movies (title TEXT, year INTEGER, genre TEXT)')
print('Table created successfully')

# close database connection
connection.close()
