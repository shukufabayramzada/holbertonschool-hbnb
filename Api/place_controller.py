from flask import Blueprint, request, jsonify
from Model.place import Place
from Persistence.data_manager import DataManager

place_controller = Blueprint('place_controller', __name__)
data_manager = DataManager() 

@place_controller.route('/places', methods=['POST'])
def post_place():
    data = request.get_json()
    id = data.get('id')
    created_at = data.get('created_at')
    updated_at = data.get('updated_at')
    description = data.get('description')
    address = data.get('address')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host = data.get('host')
    number_of_rooms = data.get('number_of_rooms')
    bath_rooms = data.get('bath_rooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenities = data.get('amenities')
    reviews = data.get('reviews')
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "Name is required"}), 400  
    
    
    # Create Place object with all attributes
    place = Place(
        id=id,
        created_at=created_at,
        updated_at=updated_at,
        description=description,
        address=address,
        latitude=latitude,
        longitude=longitude,
        host=host,
        number_of_rooms=number_of_rooms,
        bath_rooms=bath_rooms,
        price_per_night=price_per_night,
        max_guests=max_guests,
        amenities=amenities,
        reviews=reviews,
        name=name
    )
    data_manager.save(place)
    return jsonify(place.__dict__), 201

@place_controller.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place_data = data_manager.get(entity_id=place_id, entity_type='Place')
    if place_data is None:
        return jsonify({"error": "Place not found"}), 404
    
    # Check if city_data is a dictionary or an instance of City
    if isinstance(place_data, dict):
        return jsonify(place_data), 200
    else:
        return jsonify(place_data.__dict__), 200


@place_controller.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    existing_place = data_manager.get(entity_id=place_id, entity_type='Place')
    if existing_place is None:
        return jsonify({"error": "Place is not found"}), 404
    
    updated_data = {
        'id': place_id,
        'created_at': existing_place['created_at'],
        'updated_at': data.get('updated_at', existing_place['updated_at']),
        'description': data.get('description', existing_place['description']),
        'name': data.get('name', existing_place['name']),
        'address': data.get('adress', existing_place['address']),
        'latitude': data.get('latitude', existing_place['latitude']),
        'longitude': data.get('longitude', existing_place['longitude']),
        'host': data.get('host', existing_place['host']),
        'number_of_rooms': data.get('number_of_rooms', existing_place['number_of_rooms']),
        'bath_rooms': data.get('bath_rooms', existing_place['bath_rooms']),
        'price_per_night': data.get('price_per_night', existing_place['price_per_night']),
        'max_guests': data.get('max_guests', existing_place['max_guests']),
        'amenities': data.get('amenities', existing_place['amenities']),
        'reviews': data.get('reviews', existing_place['reviews'])
    }
    updated_place = Place(**updated_data)
    data_manager.update(updated_place)
    return jsonify(updated_place.__dict__), 200

@place_controller.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = data_manager.get(entity_id=place_id, entity_type='Place')
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    
    data_manager.delete(entity_id=place_id, entity_type='Place')
    return jsonify({'message': 'Place deleted'}), 204