import sqlite3

try:
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    print('Successfully connected to database')
    version = cursor.execute('select sqlite_version();')
    print(f'Version: {version.fetchall()}')

    table_creating = cursor.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY UNIQUE,
        name TEXT,
        surname TEXT,
        email TEXT NOT NULL,
        salary INTEGER);''')
    db.commit()
    print('Table created')

    inserting_data = cursor.execute('''INSERT INTO users(id,name,surname,email,salary) VALUES 
        (1, 'John', 'Malkov', 'john@gmail.com', 1000),
        (2, 'Bill', 'Jackob', 'bill@gmail.com', 1000),
        (3, 'Jane', 'Jimmys', 'jane@mail.com', 2000),
        (4, 'Josh', 'Jakies', 'josh@gmail.com', 3000);''')
    db.commit()
    print('Data inserted\n')

    print('Select all data:')
    select_data = cursor.execute('''SELECT * FROM users''')
    data = cursor.fetchall()
    for entry in data:
        print(f'{entry}\n')

    print('Select unique values:')
    select_unique_data = cursor.execute('''SELECT DISTINCT salary FROM users''')
    unique_data = cursor.fetchall()
    for entry in unique_data:
        print(f'{entry}\n')
    cursor.close()


except sqlite3.Error as error:
    print(error)
finally:
    if (db):
        db.close()
        print('Connection closed')
