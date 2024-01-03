import sqlite3


def create_table():
    connection = sqlite3.connect('sample.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    email TEXT)''')

    connection.commit()
    connection.close()


def insert_data(name, age, email):
    connection = sqlite3.connect('sample.db')
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO users (name, age, email) VALUES (?, ?, ?)''', (name, age, email))

    connection.commit()
    connection.close()


def retrieve_data():
    connection = sqlite3.connect('sample.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM users''')
    data = cursor.fetchall()

    connection.close()
    return data


create_table()


insert_data('ritik', 21, 'ritik@.com')
insert_data('rohan', 20, 'rohan@2345.com')


retrieved_data = retrieve_data()
for row in retrieved_data:
    print(row)