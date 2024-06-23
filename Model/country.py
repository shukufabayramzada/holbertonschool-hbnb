from Model.baseclass import BaseClass
from Model.city import City
from Persistence.data_manager import DataManager

class Country(BaseClass):
    def __init__(self, id=None, name=None, country_code=None):
        if id:
            self.id = id
        else:
            super().__init__()

        self.name = name
        self.country_code = country_code
    
    @staticmethod
    def get_all_countries():
        data_manager = DataManager()
        countries_data = data_manager.get_all('Country')
        countries = [Country(**data) for data in countries_data]
        return countries
    
    @staticmethod
    def get_country_by_code(country_code):
        data_manager = DataManager()
        countries_data = data_manager.get_all('Country')
        for country_data in countries_data:
            if country_data['country_code'] == country_code:
                return Country(**country_data)
        return None
    
    @staticmethod
    def get_cities_by_country_code(country_code):
        data_manager = DataManager()
        cities_data = data_manager.get_all('City')
        cities = [City(**data) for data in cities_data if data['country_code'] == country_code]
        return cities
    
    def country_code_check(self, country_code):
        if country_code.isalnum():
            return True
        raise ValueError("Country code must be alphanumeric")