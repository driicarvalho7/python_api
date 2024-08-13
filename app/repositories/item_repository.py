from app.models.item import Item

class ItemRepository:
    def __init__(self):
        self.items = [
            Item(1, "Item 1", "Descrição do Item 1"),
            Item(2, "Item 2", "Descrição do Item 2")
        ]

    def get_all(self):
        return [item.to_dict() for item in self.items]

    def get_by_id(self, item_id):
        item = next((item for item in self.items if item.id == item_id), None)
        return item.to_dict() if item else None

    def create(self, data):
        new_item = Item(len(self.items) + 1, data['name'], data['description'])
        self.items.append(new_item)
        return new_item.to_dict()

    def update(self, item_id, data):
        item = next((item for item in self.items if item.id == item_id), None)
        if item:
            item.name = data.get('name', item.name)
            item.description = data.get('description', item.description)
            return item.to_dict()
        return None

    def delete(self, item_id):
        item = next((item for item in self.items if item.id == item_id), None)
        if item:
            self.items.remove(item)
            return True
        return False
