from flask import Blueprint, jsonify, request
from Model.amenity import Amenities 
from Persistence.data_manager import DataManager

amenity_controller = Blueprint('amenity_controller', __name__)
data_manager = DataManager()

@amenity_controller.route('/amenities', methods=['POST'])
def post_amenity():
    data = request.get_json()
    id = data.get('id')
    created_at = data.get('created_at')
    updated_at = data.get('updated_at')
    description = data.get('description')
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "Name is required"}), 400  
    
    amenity = Amenities(
        id=id,
        created_at=created_at,
        updated_at=updated_at,
        description=description,
        name=name
    )
    data_manager.save(amenity)
    return jsonify(amenity.__dict__), 201

@amenity_controller.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = data_manager.get_all('Amenities')
    return jsonify(amenities), 200


@amenity_controller.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity_data = data_manager.get(entity_id=amenity_id, entity_type= 'Amenities')
    if amenity_data is None:
        return jsonify({"error": "Amenity id not found"}), 404
      
    # Check if amenity_data is a dictionary or an instance of Amenities
    if isinstance(amenity_data, dict):
        return jsonify(amenity_data), 200
    else:
        return jsonify(amenity_data.__dict__), 200
    
    
@amenity_controller.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    existing_amenity = data_manager.get(entity_id=amenity_id, entity_type='Amenities')
    if existing_amenity is None:
        return jsonify({"error": "Amenity is not found"}), 404
    
    print("helo")
    updated_data = {
        'id': amenity_id,
        'created_at': existing_amenity['created_at'],
        'updated_at': data.get('updated_at', existing_amenity['updated_at']),
        'description': data.get('description', existing_amenity['description']),
        'name': data.get('name', existing_amenity['name'])
    }
    updated_amenity = Amenities(**updated_data)
    data_manager.update(updated_amenity)
    return jsonify(updated_amenity.__dict__), 200

@amenity_controller.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    existing_amenity = data_manager.get(entity_id=amenity_id, entity_type='Amenities')
    if existing_amenity is None:
        return jsonify({"error": "Amenity is not found at all"}), 404
    data_manager.delete(entity_id=amenity_id, entity_type='Amenities')
    return jsonify({'message': 'Amenity deleted'}), 204      
