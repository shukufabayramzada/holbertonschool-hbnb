from flask import Flask, request, jsonify
from Persistence.data_manager import DataManager
from Model.city import City

city_control = Flask(__name__)
data_manager = DataManager()

@city_control.route('/city', method=['POST'])
def post_city():
    data = request.get_json()
    city = City(data['id'], data['name'], data['description'])
    # save the city to the database/ Check this code
    data_manager.save(city)
    # print city for now
    print(city)
    return jsonify(city.__dict__), 201

@city_control.route('/city/<city_id>', method=['GET'])
def get_city(city_id):
    city = data_manager.get(entity_id=city_id, entity_type= 'City')
    if city is None:
        return f({"error": "City not found"}), 404
    return jsonify(city.__dict__), 200