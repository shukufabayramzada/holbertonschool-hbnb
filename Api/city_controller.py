from flask import Flask, request, jsonify, Blueprint
from Persistence.data_manager import DataManager
from Model.city import City

city_control = Blueprint('city_controller', __name__)
data_manager = DataManager()

@city_control.route('/city', methods=['POST'])
def post_city():
    data = request.get_json()
    city_id = data.get('id')
    created_at = data.get('created_at')
    updated_at = data.get('updated_at')
    city_name = data.get('name')
    country_id = data.get('country_id')
    city = City(city_id, created_at, updated_at, city_name, country_id)
    
    data_manager.save(city)
    return jsonify(city.__dict__), 201

@city_control.route('/city/<city_id>', methods=['GET'])
def get_city(city_id):
    city_data = data_manager.get(entity_id=city_id, entity_type='City')
    if city_data is None:
        return jsonify({"error": "City not found"}), 404
    
    # Check if city_data is a dictionary or an instance of City
    if isinstance(city_data, dict):
        return jsonify(city_data), 200
    else:
        return jsonify(city_data.__dict__), 200
