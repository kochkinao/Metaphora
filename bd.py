import sqlite3

con = sqlite3.connect('save_message.db')
# select cursor
cursor = con.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT exists data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER UNIQUE,
                good INTEGER,
                normal INTEGER,
                bad INTEGER)                
                """)

def set_good(i):
    cursor.execute(f"SELECT good from data WHERE id = 1")
    a = cursor.fetchone()
    b = a[0] + 1
    cursor.execute(f"UPDATE data SET good = {b} WHERE id = 1")
    con.commit()

def set_normal(i):
    cursor.execute(f"SELECT good from data WHERE id = 1")
    a = cursor.fetchone()
    b = a[0] + 1
    cursor.execute(f"UPDATE data SET normal = {b} WHERE id = 1")
    con.commit()

def set_bad(i):
    cursor.execute(f"SELECT good from data WHERE id = 1")
    a = cursor.fetchone()
    b = a[0] + 1
    cursor.execute(f"UPDATE data SET bad = {b} WHERE id = 1")
    con.commit()

def set_chat_id(id):
    cursor.execute(f"INSERT OR IGNORE INTO data (chat_id) VALUES ({id})")
    con.commit()

def getting_the_nuber_of_users(value):
    sqlite_select_query = """SELECT * from data"""
    cursor.execute(sqlite_select_query)
    i = value + len(cursor.fetchall())
    return i

def getting_good(i):
    cursor.execute(f"SELECT (good) from data WHERE id = 1")
    a = cursor.fetchone()
    i = a[0] + i
    return i

def getting_normal(i):
    cursor.execute(f"SELECT (normal) from data WHERE id = 1")
    a = cursor.fetchone()
    i = a[0] + i
    return i

def getting_bad(i):
    cursor.execute(f"SELECT (bad) from data WHERE id = 1")
    a = cursor.fetchone()
    i = a[0] + i
    return i