import sqlite3

con = sqlite3.connect('save_message.db')
# select cursor
cursor = con.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT exists data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER UNIQUE,
                message TEXT)                
                """)

def set_chat_id(id):
    cursor.execute(f"INSERT OR IGNORE INTO data (chat_id) VALUES ({id})")
    con.commit()

def getting_the_nuber_of_users(value):
    sqlite_select_query = """SELECT * from data"""
    cursor.execute(sqlite_select_query)
    i = value + len(cursor.fetchall())
    return i