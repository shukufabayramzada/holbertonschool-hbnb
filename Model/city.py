from Model.baseclass import BaseClass

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
    
    def country_id_check(self, country_id):
        if country_id.isnumeric():
            return True
        raise ValueError("Area code must be in numbers")