from flask import Flask, request, jsonify, Blueprint
from Persistence.data_manager import DataManager
from Model.country import Country

country_controller = Blueprint('country_controller', __name__)
data_manager = DataManager()

@country_controller.route('/country', methods=['POST'])
def post_country():
    data = request.get_json()
    self_id = data.get('id')
    country_name = data.get('name')
    country_id = data.get('country_id')
    country = Country(self_id, country_name, country_id)
    
    data_manager.save(country)
    return jsonify(country.__dict__), 201

@country_controller.route('/country/<country_id>', methods=['GET'])
def get_country(country_id):
    country_data = data_manager.get(entity_id=country_id, entity_type='country')
    if country_data is None:
        return jsonify({"error": "country not found"}), 404
    
    # Check if country_data is a dictionary or an instance of country
    if isinstance(country_data, dict):
        return jsonify(country_data), 200
    else:
        return jsonify(country_data.__dict__), 200
