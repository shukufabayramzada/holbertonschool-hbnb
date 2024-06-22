#!/usr/bin/python3
from Persistence.i_persistence import IPersistenceManager
import json
import os

class DataManager(IPersistenceManager):
    def __init__(self, storage_file="data.json"):
        self.storage_file = storage_file
        if not os.path.exists(storage_file):
            with open(storage_file, "w") as f:
                f.write("{}")
                
    def _load_data(self):
        with open(self.storage_file, "r") as f:
            return json.load(f)
        
    def _write_data(self, data):
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)
            
    def save(self, entity):
        with open(self.storage_file, "r") as f:
            data = json.load(f)
        entity_id = getattr(entity, "id")
        entity_type = type(entity).__name__
        if entity_type not in data:
            data[entity_type] = {}
        data[entity_type][entity_id] = entity.__dict__
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)
            
            
    def get(self, entity_id = "", entity_type = ""):
        data = self._load_data()
        if entity_type in data and str(entity_id) in data[entity_type]:
            return data[entity_type][str(entity_id)]
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")
            
    def get_all(self, entity_type):
        data = self._load_data()
        if entity_type in data:
            return list(data[entity_type].values())
        return []
    
    def update(self, entity):
        data = self._load_data()
        entity_id = getattr(entity, "id")
        entity_type = type(entity).__name__
        if entity_type in data and str(entity_id) in data[entity_type]:
            data[entity_type][entity_id] = entity.__dict__
            self._write_data(data)
            print(f"Entity {entity_type} with id {entity_id} updated.")
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")
            
    def delete(self, entity_id, entity_type):
        data = self._load_data()
        if entity_type in data and str(entity_id) in data[entity_type]:
            del data[entity_type][str(entity_id)]
            self._write_data(data)
            print(f"Entity {entity_type} with id {entity_id} deleted.")
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")