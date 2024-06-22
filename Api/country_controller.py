from flask import Flask, request, jsonify, Blueprint
from Persistence.data_manager import DataManager
from Model.country import Country

country_controller = Blueprint('country_controller', __name__)
data_manager = DataManager()

@country_controller.route('/country', methods=['POST'])
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


@country_controller.route('/countries/<country_id>', methods=['GET'])
def get_country(country_id):
    country = data_manager.get(entity_id=country_id, entity_type='Country')
    return jsonify(country.__dict__), 200