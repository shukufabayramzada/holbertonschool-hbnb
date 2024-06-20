#!/usr/bin/python3
import unittest
from datetime import datetime
from Model.place import Place
from Model.user import User
from Model.review import Reviews


"""
This test support Business Rule Enforcement in which we need to have
review restrictions for hosts, and Check for adding valid rating
to reviews
"""

class TestReviews(unittest.TestCase):
    
    
    """Test that a place owner cannot review their own place."""
    
    def test_not_own_review(self):
        # Create a user who is also a host
        updated_at = datetime.now()
        created_at = datetime.now()
        host_id = 1
        place_id = 1
        host = User(id=host_id, created_at=created_at, updated_at=updated_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!", email="owner@email.com",
                     first_name="Host", last_name="Owner")
        place = Place(id=place_id, created_at=created_at,
                      updated_at=updated_at,
                      name="Place test", description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, price_per_night=100,
                      max_guests=6, host=host,
                      number_of_rooms=3, bath_rooms=2, amenities=5,
                      reviews=13)

        # Attempt to review own place
        review_text = "Great place to stay!"
        with self.assertRaises(ValueError):
            host.not_own_review(host_id, place_id, review_text)
            
    
    """
    Test for checking ratings
    """
    def setUp(self):
        self.review = Reviews(id="1", created_at="2024-06-20", updated_at="2024-06-20", place="Place1", rating=3, comment="Nice place")

    def test_add_valid_rating(self):
        # Test with a valid rating
        self.review.add_rating(5)
        self.assertEqual(self.review.rating, 5)

    def test_add_invalid_rating_too_low(self):
        # Test with an invalid rating (too low)
        with self.assertRaises(ValueError) as context:
            self.review.add_rating(0)
        self.assertEqual(str(context.exception), "Ratings must be from 1 to 5")

    def test_add_invalid_rating_too_high(self):
        # Test with an invalid rating (too high)
        with self.assertRaises(ValueError) as context:
            self.review.add_rating(6)
        self.assertEqual(str(context.exception), "Ratings must be from 1 to 5")

if __name__ == '__main__':
    unittest.main()