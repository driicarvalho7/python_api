from flask import Blueprint, request, jsonify
from app.use_cases.user_use_cases import UserUseCases

user_blueprint = Blueprint('users', __name__)

# Instância do caso de uso
user_use_cases = UserUseCases()

# GET /users
@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = user_use_cases.get_all_users()
    return jsonify(users), 200

# GET /users/{id}
@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_use_cases.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User não encontrado"}), 404

# POST /users
@user_blueprint.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = user_use_cases.create_user(data)
    return jsonify(new_user), 201

# PUT /users/{id}
@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = user_use_cases.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user), 200
    else:
        return jsonify({"error": "User não encontrado"}), 404

# DELTE /users/{id}
@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = user_use_cases.delete_user(user_id)
    if success:
        return jsonify({"message": "success"}), 200
    else:
        return jsonify({"error": "User não encontrado"}), 404
