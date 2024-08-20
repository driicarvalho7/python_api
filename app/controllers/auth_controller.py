from flask import Blueprint, request, jsonify
from app.use_cases.auth_use_cases import AuthUseCases
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

auth_blueprint = Blueprint('auth', __name__)

auth_use_cases = AuthUseCases()

# Endpoint de login para obter o token JWT
@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = auth_use_cases.authenticate_user(data['email'], data['password'])
    if user:
        access_token = create_access_token(identity=user['id'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciais inválidas"}), 401

# Exemplo de endpoint protegido (opcional)
@auth_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify(logged_in_as=current_user_id), 200
