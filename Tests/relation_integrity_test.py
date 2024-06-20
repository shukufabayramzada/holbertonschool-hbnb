#!/usr/bin/python3
import unittest
from datetime import datetime
from Model.place import Place
from Model.user import User
from Model.review import Reviews

"""
Test is designed for testing the integrity of relationships
between objects, such as
places to their host users and reviews to their corresponding
places
"""

class TestIntegrity(unittest.TestCase):
    
    def test_relationship_integrity(self):
        """Test relationship integrity."""
        User.users = []
        updated_at = datetime.now()
        created_at = datetime.now()
        user = User(id=1, created_at=created_at, updated_at=updated_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!", email="user@email.com",
                     first_name="Michael",
                     last_name="Hernandez")
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place Test", description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=user,
                      price_per_night=100, max_guests=6,
                      number_of_rooms=3, bath_rooms=2, amenities=5,
                      reviews=13)
        review = Reviews(id=1, created_at=created_at, updated_at=updated_at,
                         place=place,
                         rating=5, comment="Amazing experience!")
        self.assertEqual(place.host, user)
        self.assertEqual(review.place, place)
        
if __name__ == '__main__':
    unittest.main()