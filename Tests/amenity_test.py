#!/usr/bin/python3
import unittest
from datetime import datetime
from Model.place import Place


class TestAmenity(unittest.TestCase):

    def test_amenity_addition(self):
        """Test amenity addition."""
        created_at = datetime.now()
        updated_at = datetime.now()
        place = Place(id=1, created_at=created_at, updated_at=updated_at, name="Place test",
                      description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370,
                      host=None, price_per_night=100, max_guests=6,
                      number_of_rooms=2, bath_rooms=1, amenities=2,
                      reviews=10)
        place.add_amenity("Wi-Fi")
        place.add_amenity("Pool")
        self.assertCountEqual(place.amenities, ["Wi-Fi", "Pool"])

    def test_retrieve_and_update_amenities(self):
        """Test retrieve and update amenities."""
        updated_at = datetime.now()
        created_at = datetime.now()
        place = Place(id=1, created_at=created_at, updated_at=updated_at,
                      name="Place test", description="Test description",
                      address="420 Test street",
                      latitude=48.8584, longitude=2.3370, host=None,
                      price_per_night=100, max_guests=6,
                      number_of_rooms=3, bath_rooms=2, amenities=5,
                      reviews=13)
        place.add_amenity("Wi-Fi")
        place.update_amenity("Wi-Fi", "High-speed Wi-Fi")
        self.assertIn("High-speed Wi-Fi", place.amenities)
        
if __name__ == '__main__':
    unittest.main()