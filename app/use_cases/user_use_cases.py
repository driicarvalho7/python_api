from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

class UserUseCases:
    def __init__(self):
        self.user_repository = UserRepository()

    #CRUD GERAL
    def get_all_users(self):
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def create_user(self, data):
        # Hash da senha antes de salvar no banco
        data['password'] = generate_password_hash(data['password'])
        return self.user_repository.create(data)

    # No seu arquivo user_use_cases.py
    def update_user(self, user_id, data):
        if 'password' in data:
            data['password'] = generate_password_hash(data['password'], method='pbkdf2:sha256')
        return self.user_repository.update(user_id, data)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)
    #END