from flask import Flask, request, jsonify
from Persistence.data_manager import DataManager
from Model.country import Country

app = Flask(__name__)
data_manager = DataManager()

@app.route('/country', methods=['POST'])
def post_country():
    data = request.get_json()
    country = Country(data['id'], data['name'], data['description'])
    # save the country to the database
    data_manager.save(country)
    # print country for now
    print(country)
    return jsonify(country.__dict__), 201 


@app.route('/countries/<country_id>', methods=['GET'])
def get_country(country_id):
    country = data_manager.get(entity_id=country_id, entity_type='Country')
    return jsonify(country.__dict__), 200