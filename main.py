from flask import Flask
from app.controllers.item_controller import item_blueprint
from app.controllers.user_controller import user_blueprint
from app.controllers.auth_controller import auth_blueprint
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-key')  # Substitua por uma chave segura
jwt = JWTManager(app)

# Registrar os blueprints dos controllers
app.register_blueprint(item_blueprint, url_prefix='/items')
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
