import unittest
import os
import json
from unittest.mock import MagicMock
from Persistence.data_manager import DataManager

class MockEntity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TestDataManager(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_data.json"
        self.data_manager = DataManager(self.test_file)
        # Ensure the test file is clean
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        # Re-create the DataManager to ensure it creates a new empty file
        self.data_manager = DataManager(self.test_file)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_save_entity(self):
        entity = MockEntity("1", "Test Entity")
        self.data_manager.save(entity)
        
        with open(self.test_file, "r") as f:
            data = json.load(f)
        
        self.assertIn("MockEntity", data)
        self.assertIn("1", data["MockEntity"])
        self.assertEqual(data["MockEntity"]["1"]["name"], "Test Entity")
    
    def test_get_entity(self):
        entity = MockEntity("1", "Test Entity")
        self.data_manager.save(entity)
        
        retrieved_entity = self.data_manager.get("1", "MockEntity")
        
        self.assertEqual(retrieved_entity["name"], "Test Entity")
    
    def test_get_all_entities(self):
        entity1 = MockEntity("1", "Test Entity 1")
        entity2 = MockEntity("2", "Test Entity 2")
        self.data_manager.save(entity1)
        self.data_manager.save(entity2)
        
        all_entities = self.data_manager.get_all("MockEntity")
        
        self.assertEqual(len(all_entities), 2)
        self.assertEqual(all_entities[0]["name"], "Test Entity 1")
        self.assertEqual(all_entities[1]["name"], "Test Entity 2")
    
    def test_update_entity(self):
        entity = MockEntity("1", "Test Entity")
        self.data_manager.save(entity)
        
        entity.name = "Updated Entity"
        self.data_manager.update(entity)
        
        updated_entity = self.data_manager.get("1", "MockEntity")
        
        self.assertEqual(updated_entity["name"], "Updated Entity")
    
    def test_delete_entity(self):
        entity = MockEntity("1", "Test Entity")
        self.data_manager.save(entity)
        
        self.data_manager.delete("1", "MockEntity")
        
        deleted_entity = self.data_manager.get("1", "MockEntity")
        
        self.assertIsNone(deleted_entity)
    
if __name__ == "__main__":
    unittest.main()
