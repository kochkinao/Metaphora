import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.connection_cursor = self.connection.cursor()
        self.cursor = self.connection_cursor

    def all_users(self):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM data").fetchall()
            return len(result)

    def user_exsits(self, user_id):
        result = self.cursor.execute("SELECT user_id FROM data WHERE user_id = ?", (user_id,)).fetchall()
        return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'data' ('user_id') VALUES (?)", (user_id,))

    def add_start_user(self):
        with self.connection:
            a = self.cursor.execute("SELECT start FROM data WHERE id = 1").fetchone()
            b = a[0] + 1
            self.cursor.execute(f"UPDATE data SET start = {b} WHERE id = 1")

    def get_start_user(self):
        with self.connection:
            result = self.cursor.execute("SELECT start FROM data WHERE id = 1").fetchone()
            return result[0]

    def add_good(self):
        with self.connection:
            a = self.cursor.execute("SELECT good FROM data WHERE id = 1").fetchone()
            b = a[0] + 1
            self.cursor.execute(f"UPDATE data SET good = {b} WHERE id = 1")

    def add_normal(self):
        with self.connection:
            a = self.cursor.execute("SELECT normal FROM data WHERE id = 1").fetchone()
            b = a[0] + 1
            self.cursor.execute(f"UPDATE data SET normal = {b} WHERE id = 1")

    def add_bad(self):
        with self.connection:
            a = self.cursor.execute("SELECT bad FROM data WHERE id = 1").fetchone()
            b = a[0] + 1
            self.cursor.execute(f"UPDATE data SET bad = {b} WHERE id = 1")

    def get_good(self):
        with self.connection:
            result = self.cursor.execute("SELECT good FROM data WHERE id = 1").fetchone()
            return result[0]

    def get_normal(self):
        with self.connection:
            result = self.cursor.execute("SELECT normal FROM data WHERE id = 1").fetchone()
            return result[0]

    def get_bad(self):
        with self.connection:
            result = self.cursor.execute("SELECT bad FROM data WHERE id = 1").fetchone()
            return result[0]

    def get_user(self):
        return self.cursor.execute("SELECT user_id FROM data").fetchall()