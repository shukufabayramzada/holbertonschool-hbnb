from .baseclass import Baseclass

class Amenities(Baseclass):
    
    def __init__(self, name, description, id, created_at, updated_at):
        super.__init__(id, created_at, updated_at)
        self.name = name
        self.description = description
    
    def add_place(self, place):
        self.places.append(place)
        
    def remove_place(self, place):
        self.places.remove(place)
        