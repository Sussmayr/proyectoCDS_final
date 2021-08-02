import sys
import pyodbc

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=DESKTOP-EV3RATL;'
                      'Database=FaceRecognition;'
                      'Trusted_Connection=yes;')


'''
cursor = conn.cursor()

def read():
    print ("read")
    cursor.execute("SELECT * from users")
    for row in cursor:
        print(f'row = {row}')
    print()

def insert():
    print("create")
    cursor.execute(
        'INSERT INTO user(Name,pass) values(?,?);',
        ('edward', 'facil123')
    )
    conn.commit()
    read(conn)

def update():
    print("update")
    cursor.execute(
        'UPDATE user set Name = ? where pass = ?;',
        ('edward', 'facil123')
    )
    conn.commit()
    read(conn)

def delete():
    print("delete")
    cursor.execute(
        'DELETE from user where id > 4;'
    )
    conn.commit()
    read(conn)

conn.close()
'''