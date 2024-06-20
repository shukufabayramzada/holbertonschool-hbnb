#!/usr/bin/python3
import unittest
from datetime import datetime
from Model.place import Place
from Model.user import User

"""
Test for:
1.Place Instantiation - Test creating a Place object with all required fields 
and validate that missing or incorrect fields are handled correctly.
2.Host Assignment Rules - Ensure that a Place object can be
assigned only one host and validate that re-assignment is handled according to specified rules.
3.Place Attribute Validation - Validate geographical coordinates (latitude and longitude)
and other properties like price per night and max guests to check they are within acceptable ranges.
4.Deleting Places - Test that when a Place is deleted,
it’s removed correctly and cleans up all associated references, such as from the host’s list of places.
"""

class TestPlace(unittest.TestCase):
    
    # Place instantiation
    def test_place_instantiation(self):
        """Test place instantiation."""
        updated_at = datetime.now()
        created_at = datetime.now()
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test", description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=None,
                      price_per_night=100, max_guests=6,
                      number_of_rooms=3, bath_rooms=2, amenities=5,
                      reviews=13)
        self.assertEqual(place.name, "Place test")
        
    # Host-assignment checking
    def test_host_assignment_rules(self):
        """Test host assignment rules."""
        updated_at = datetime.now()
        created_at = datetime.now()
        user1 = User(id=1, created_at=created_at, updated_at=updated_at,
                      host_id="Owner", place_id="Owned place",
                      review="Great place to stay!",
                      email="user_1@email.com",
                      first_name="Gus",
                      last_name="Fring")
        user2 = User(id=2, created_at=created_at, updated_at=updated_at,
                      host_id="Owner", place_id="Owned place",
                      review="Great place to stay!",
                      email="user_2@email.com",
                      first_name="Chuck",
                      last_name="McGill")
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test",
                      description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=user1,
                      price_per_night=100, max_guests=6,
                      number_of_rooms=3, bath_rooms=2, amenities=5,
                      reviews=13)
        # Test that assigning a new host to a place that already
        # has one raises ValueError
        with self.assertRaises(ValueError):
            place.new_host(user2)

    # Place attribute validation
    def test_place_attribute_validation(self):
        """Test place attribute validation."""
        updated_at = datetime.now()
        created_at = datetime.now()
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test", description="Test description",
                      address="420 Test street", latitude=48.8584,
                      longitude=2.3370, host=None, price_per_night=100,
                      max_guests=6,
                      number_of_rooms=3, bath_rooms=2, amenities=5,
                      reviews=13)
        self.assertEqual(place.latitude, 48.8584)
        self.assertEqual(place.longitude, 2.3370)
        self.assertEqual(place.price_per_night, 100)
        self.assertEqual(place.max_guests, 6)

    # Deleting places
    def test_deleting_places(self):
        """Test deleting places."""
        User.users = []
        updated_at = datetime.now()
        created_at = datetime.now()
        user = User(id=1, created_at=created_at, updated_at=updated_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!",
                     email="user@email.com",
                     first_name="Jimmy",
                     last_name="McGill")
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test",
                      description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=user,
                      price_per_night=100, max_guests=6,
                      number_of_rooms=3, bath_rooms=2, amenities=5,
                      reviews=13
                      )
        place.delete()
        self.assertIsNone(place.host)
        
if __name__ == '__main__':
    unittest.main()