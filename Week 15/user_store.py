import sqlite3
import json

class UserStore:

    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db() 

    def init_db(self):

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id      INTEGER PRIMARY KEY,
                name    TEXT NOT NULL,
                email   TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    def load(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()

        connection.close()

        users = []
        for row in rows:
            users.append({
                "id":    row[0],
                "name":  row[1],
                "email": row[2]
            })

        return users

    def save(self, user):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user["name"], user["email"])
        )

        new_id = cursor.lastrowid

        connection.commit()
        connection.close()

        return new_id

    def find_by_id(self, user_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, name, email FROM users WHERE id = ?",
            (user_id,)
        )
        row = cursor.fetchone()

        connection.close()

        if row is None:
            return None

        return {
            "id":    row[0],
            "name":  row[1],
            "email": row[2]
        }

    def update_user(self, user_id, updated_data):
        existing_user = self.find_by_id(user_id)

        if existing_user is None:
            return False

        new_name  = updated_data.get("name",  existing_user["name"])
        new_email = updated_data.get("email", existing_user["email"])

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (new_name, new_email, user_id)
        )

        connection.commit()
        connection.close()

        return True  

    def delete_user(self, user_id):
        existing_user = self.find_by_id(user_id)

        if existing_user is None:
            return False 

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

        connection.commit()
        connection.close()

        return True  
