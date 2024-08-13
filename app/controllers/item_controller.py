from flask import Blueprint, request, jsonify
from app.use_cases.item_use_cases import ItemUseCases

item_blueprint = Blueprint('items', __name__)

# Instância do caso de uso
item_use_cases = ItemUseCases()

# GET /items
@item_blueprint.route('/', methods=['GET'])
def get_items():
    items = item_use_cases.get_all_items()
    return jsonify(items), 200

# GET /items/{id}
@item_blueprint.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = item_use_cases.get_item_by_id(item_id)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item não encontrado"}), 404

# POST /items
@item_blueprint.route('/', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = item_use_cases.create_item(data)
    return jsonify(new_item), 201

# PUT /items/{id}
@item_blueprint.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    updated_item = item_use_cases.update_item(item_id, data)
    if updated_item:
        return jsonify(updated_item), 200
    else:
        return jsonify({"error": "Item não encontrado"}), 404

# DELTE /items/{id}
@item_blueprint.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    success = item_use_cases.delete_item(item_id)
    if success:
        return jsonify({"message": "success"}), 200
    else:
        return jsonify({"error": "Item não encontrado"}), 404
