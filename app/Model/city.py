from baseclass import BaseClass

class City(BaseClass):
    
    def __init__(self, id, created_at, updated_at, name, country_id):
        super.__init__(id, created_at, updated_at)
        self.name = name
        self.country_id = country_id
    
    def country_id_check(self, country_id):
        if country_id.isnumeric():
            return True
        raise ValueError("Area code must be in numbers")