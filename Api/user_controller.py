from flask import Blueprint, request, jsonify
from Persistence.data_manager import DataManager  # from Main Model module
from datetime import datetime
from Model.user import User

user_controller = Blueprint('user_controller', __name__)
data_manager = DataManager()

@user_controller.route('/users', methods=['POST'])
def post_user():
    """Creates new user"""
    data = request.get_json()
    id = data.get('id')
    created_at = data.get('created_at')
    updated_at = data.get('updated_at')
    first_name = data.get('first_name')
    email = data.get('email')
    last_name = data.get('last_name')
    host_id = data.get('host_id')
    place_id = data.get('place_id')
    reviews = data.get('reviews')
    

    if not email or not first_name or not last_name:
        return jsonify({'error': 'Missing required fields'}), 400

    if '@' not in email:  # Simple email validation
        return jsonify({'error': 'Invalid email format'}), 400

    if User.email_check(email):
        return jsonify({'error': 'Email already exists'}), 409

    user = User(
        id=id,
        created_at=created_at,
        updated_at=updated_at,
        first_name=first_name,
        last_name=last_name,
        email=email,
        host_id=host_id,
        place_id=place_id,
        reviews=reviews       
    )
    data_manager.save(user)
    return jsonify(user.__dict__), 201

@user_controller.route('/users', methods=['GET'])
def get_users():
    users = data_manager.get_all('User')
    return jsonify(users), 200

@user_controller.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = data_manager.get(user_id, 'User')
    if user_data is None:
        return jsonify({'error': 'User not found'}), 404
    
    # Check if user_data is a dictionary or an instance of User
    if isinstance(user_data, dict):
        return jsonify(user_data), 200
    else:
        return jsonify(user_data.__dict__), 200

@user_controller.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user by id"""
    data = request.get_json()

    existing_user_data = data_manager.get(user_id, 'User')
    if not existing_user_data:
        return jsonify({'error': 'User not found'}), 404

    email = data.get('email')
    if email:
        if '@' not in email: 
            return jsonify({'error': 'Invalid email format'}), 400
        if email != existing_user_data['email'] and User.email_check(email):
            return jsonify({'error': 'Email already exists'}), 409
        
    updated_data = {
        'id': user_id,
        'created_at': existing_user_data['created_at'],
        'updated_at': data.get('updated_at', existing_user_data['updated_at']),
        'first_name': data.get('first_name', existing_user_data['first_name']),
        'last_name': data.get('last_name', existing_user_data['last_name']),
        'email': email or existing_user_data['email'],
        'host_id': data.get('host_id', existing_user_data['host_id']),
        'place_id': data.get('place_id', existing_user_data['place_id']),
        'reviews': data.get('reviews', existing_user_data['reviews'])
    }

    updated_user = User(**updated_data)
    data_manager.update(updated_user)

    return jsonify(updated_user.__dict__), 200

@user_controller.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes user by id"""
    user = data_manager.get(user_id, 'User')
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data_manager.delete(user_id, 'User')
    return jsonify({'message': 'User deleted'}), 204
