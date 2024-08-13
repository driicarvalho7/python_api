from app.repositories.item_repository import ItemRepository

class ItemUseCases:
    def __init__(self):
        self.item_repository = ItemRepository()

    def get_all_items(self):
        return self.item_repository.get_all()

    def get_item_by_id(self, item_id):
        return self.item_repository.get_by_id(item_id)

    def create_item(self, data):
        return self.item_repository.create(data)

    def update_item(self, item_id, data):
        return self.item_repository.update(item_id, data)

    def delete_item(self, item_id):
        return self.item_repository.delete(item_id)
