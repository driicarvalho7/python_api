from app.models.user import User

class UserRepository:
    def __init__(self):
        self.users = [
            User(1, "Master", "master@gmail.com", "master123"),
            User(2, "Developer", "dev@gmail.com", "dev123")
        ]

    def get_all(self):
        return [user.to_dict() for user in self.users]

    def get_by_id(self, user_id):
        user = next((user for user in self.users if user.id == user_id), None)
        return user.to_dict() if user else None

    def create(self, data):
        new_user = User(len(self.users) + 1, data['name'], data['email'], data['password'])
        self.users.append(new_user)
        return new_user.to_dict()

    def update(self, user_id, data):
        user = next((user for user in self.users if user.id == user_id), None)
        if user:
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.password = data.get('password', user.password)
            return user.to_dict()
        return None

    def delete(self, user_id):
        user = next((user for user in self.users if user.id == user_id), None)
        if user:
            self.users.remove(user)
            return True
        return False
