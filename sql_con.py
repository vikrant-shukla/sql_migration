import sqlite3


def connection():
    """Sqlite db connection created"""
    
    try:
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        return cursor, sqliteConnection
    except sqlite3.Error as error:
        print('Error occurred - ', error)

def close(sqliteConnection):
    """Closing of the open sesssions of db"""

    try: 
        if sqliteConnection:
                sqliteConnection.commit()
                sqliteConnection.close()
                print('SQLite Connection closed')
    except Exception as error:
        print('Error occurred - ', error)