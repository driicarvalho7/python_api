from app.models.item import Item
from app.database import get_connection

class ItemRepository:
    def get_all(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, description FROM api_py.item")
        rows = cursor.fetchall()
        items = [Item(row[0], row[1], row[2]).to_dict() for row in rows]
        cursor.close()
        connection.close()
        return items

    def get_by_id(self, item_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, description FROM api_py.item WHERE id = %s", (item_id,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        return Item(row[0], row[1], row[2]).to_dict() if row else None

    def create(self, data):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO api_py.item (name, description) VALUES (%s, %s) RETURNING id",
            (data['name'], data['description'])
        )
        new_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()
        return Item(new_id, data['name'], data['description']).to_dict()

    def update(self, item_id, data):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE api_py.item SET name = %s, description = %s WHERE id = %s RETURNING id, name, description",
            (data['name'], data['description'], item_id)
        )
        row = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return Item(row[0], row[1], row[2]).to_dict() if row else None

    def delete(self, item_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM api_py.item WHERE id = %s RETURNING id", (item_id,))
        deleted_id = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return deleted_id is not None
