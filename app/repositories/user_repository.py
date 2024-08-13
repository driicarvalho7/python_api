from app.models.user import User
from app.database import get_connection

class UserRepository:
    def get_all(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, email, password FROM api_py.user")
        rows = cursor.fetchall()
        users = [User(row[0], row[1], row[2], row[3]).to_dict() for row in rows]
        cursor.close()
        connection.close()
        return users

    def get_by_id(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, email, password FROM api_py.user WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        return User(row[0], row[1], row[2], row[3]).to_dict() if row else None

    def create(self, data):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO api_py.user (name, email, password) VALUES (%s, %s, %s) RETURNING id",
            (data['name'], data['email'], data['password'])
        )
        new_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()
        return User(new_id, data['name'], data['email'], data['password']).to_dict()

    def update(self, user_id, data):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE api_py.user SET name = %s, email = %s, password = %s WHERE id = %s RETURNING id, name, email, password",
            (data['name'], data['email'], data['password'], user_id)
        )
        row = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return User(row[0], row[1], row[2], row[3]).to_dict() if row else None

    def delete(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM api_py.user WHERE id = %s RETURNING id", (user_id,))
        deleted_id = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return deleted_id is not None
