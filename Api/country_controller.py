from flask import Flask, request, jsonify
from Persistence.data_manager import DataManager
from Model.country import Country

coutry_controller = Flask(__name__)
data_manager = DataManager()

@coutry_controller.route('/country', methods=['POST'])
def post_country():
    data = request.get_json()
    country_id = data.get('coutry_id')
    name = data.get('name')
    country = Country(country_id=country_id, name=name)
    # save the country to the database
    data_manager.save(country)
    # print country for now
    print(country)
    return jsonify(country.__dict__), 201 


@coutry_controller.route('/countries/<country_id>', methods=['GET'])
def get_country(country_id):
    country = data_manager.get(entity_id=country_id, entity_type='Country')
    return jsonify(country.__dict__), 200