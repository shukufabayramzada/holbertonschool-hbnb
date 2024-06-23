
from Model.baseclass import BaseClass

class Amenities(BaseClass):
    def __init__(self, name, description, id=None, created_at=None, updated_at=None):
        if id:
            self.id = id
        else:
            super().__init__()  # Generate new UUID only if ID is not provided
        
        if created_at:
            self.created_at = created_at
        if updated_at:
            self.updated_at = updated_at
            
        self.name = name
        self.description = description
    
    def add_place(self, place):
        self.places.append(place)
        
    def remove_place(self, place):
        self.places.remove(place)
        
    def __str__(self):
        return "Your ID is" + str(self.name)
        