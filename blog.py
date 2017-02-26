# https://www.youtube.com/watch?v=VI9mOrRiea4

from flask import Flask, render_template, request
# 'render_template' renders templates and 'request' handles http requests

import sqlite3

app = Flask(__name__)

# connecting application to the database
connection = sqlite3.connect('database.db')
print('Database opened successfully')

# execute database commands
connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')
print('Table created successfully')

# close database connection
connection.close()

@app.route('/')
def hello_world():
    return "Hello World!"

# Rendering a template:
@app.route('/new')
def new_post():
    return render_template('new.html')

@app.route('/addrecord', methods = ['POST'])
def addrecord():
    connection = sqlite3.connect('database.db')
    # cursor lets us write in the database
    cursor = connection.cursor()

    try:
        title = request.form['title']
        post = request.form['post']
        cursor.execute('INSERT INTO posts (title,post) VALUES (?,?)', (title,post))
        connection.commit()
        message = "Record successfuly added"
    except:
        connection.rollback()
        message = "error in insert operation"
    finally:
        return render_template('result.html', message = message)
        connection.close()

if __name__ == '__main__':
    app.run(debug = True)
