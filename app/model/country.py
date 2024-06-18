class Country:
    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id
    
    def country_id_check(self, country_id):
        if country_id.isnumeric():
            return True
        raise ValueError("Area code must be number")