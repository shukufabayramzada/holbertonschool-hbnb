from Model.baseclass import BaseClass
from Persistence.data_manager import DataManager

class City(BaseClass):
    
    def __init__(self, name, country_id, id=None, created_at=None, updated_at=None):
        if id:
            self.id = id
        else:
            super().__init__()
            
        if created_at:
            self.created_at = created_at
        if updated_at:
            self.updated_at = updated_at
        
        self.name = name
        self.country_id = country_id
    
    @staticmethod
    def get_all_cities():
        data_manager = DataManager()
        cities_data = data_manager.get_all('City')
        cities = [City(**data) for data in cities_data]
        return cities

    @staticmethod
    def get_city_by_id(city_id):
        data_manager = DataManager()
        city_data = data_manager.get(city_id, 'City')
        if city_data:
            return City(**city_data)
        return None
    
    def country_id_check(self, country_id):
        if country_id.isnumeric():
            return True
        raise ValueError("Country ID must be numeric")