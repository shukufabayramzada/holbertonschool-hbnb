from flask import Blueprint, request, jsonify
from Persistence.data_manager import DataManager
from datetime import datetime
from Model.city import City
from Model.country import Country


country_city_controller = Blueprint('country_city_controller', __name__)
data_manager = DataManager()


@country_city_controller.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.get_all_countries()
    return jsonify([country.__dict__ for country in countries]), 200


@country_city_controller.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = Country.get_country_by_code(country_code)
    if country is None:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.__dict__), 200


@country_city_controller.route('/countries/<country_code>/cities',
                               methods=['GET'])
def get_cities_by_country(country_code):
    cities = City.get_cities_by_country_code(country_code)
    if cities is None:
        return jsonify({'error': 'No cities found for this country'}), 404
    return jsonify([city.__dict__ for city in cities]), 200


@country_city_controller.route('/cities', methods=['POST'])
def post_city():
    data = request.get_json()
    now = datetime()
    city = City(
        name=data['name'],
        country_code=data['country_code'],
        created_at=now,
        updated_at=now
        )
    city.save()
    return jsonify(city.__dict__), 201


@country_city_controller.route('/cities', methods=['GET'])
def get_cities():
    cities = City.get_all_cities()
    return jsonify([city.__dict__ for city in cities]), 200


@country_city_controller.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = City.get_city_by_id(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.__dict__), 200


@country_city_controller.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    existing_city = data_manager.get(entity_id=city_id, entity_type='City')
    if existing_city is None:
        return jsonify({"error": "City is not found"}), 404
    
    updated_city = {
        'id': city_id,
        'created_at': existing_city['created_at'],
        'updated_at': data.get('updated_at', existing_city['updated_at']),
        'country_id': data.get('country_id', existing_city['country_id']),
        'name': data.get('name', existing_city['name'])
    }
    updated_city = City(**updated_city)
    data_manager.update(updated_city)
    return jsonify(updated_city.__dict__), 200


@country_city_controller.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.get_city_by_id(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    city.delete()
    return jsonify({'message': 'City deleted'}), 204