
from flask import Flask, render_template, request
# 'render_template' renders templates and 'request' handles http requests

import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods = ['POST'])
def movie():
    connection = sqlite3.connect('database.db')
    print('Database opened successfully')
    # cursor lets us write in the database
    cursor = connection.cursor()

    try:
        title = request.form['title']
        year = request.form['year']
        genre = request.form['genre']
        cursor.execute('INSERT INTO movies (title,year,genre) VALUES (?,?,?)', (title,year,genre))
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
