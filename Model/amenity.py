
from Model.baseclass import BaseClass

class Amenities(BaseClass):
    
    def __init__(self, name, description, id, created_at, updated_at):
        super().__init__()
        self.name = name
        self.description = description
    
    def add_place(self, place):
        self.places.append(place)
        
    def remove_place(self, place):
        self.places.remove(place)
        
    def __str__(self):
        return "Your ID is" + str(self.name)
        