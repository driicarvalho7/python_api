from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

class AuthUseCases:
    def __init__(self):
        self.user_repository = UserRepository()

    # AUTH
    def authenticate_user(self, email, password):
        user = self.user_repository.get_by_email(email)
        if user and check_password_hash(user['password'], password):
            return user
        return None
    #END