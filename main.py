from flask import Flask
from app.controllers.item_controller import item_blueprint
from app.controllers.user_controller import user_blueprint

app = Flask(__name__)
app.register_blueprint(item_blueprint, url_prefix='/items')
app.register_blueprint(user_blueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
