import unittest
from Model.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City(id="1", created_at="2024-06-20", updated_at="2024-06-20", name="Test City", country_id="123")
        
    def test_country_id_check_valid(self):
        result = self.city.country_id_check("123")
        self.assertTrue(result)

    def test_country_id_check_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.city.country_id_check("ABC")
        self.assertEqual(str(context.exception), "Area code must be in numbers")

if __name__ == "__main__":
    unittest.main()
