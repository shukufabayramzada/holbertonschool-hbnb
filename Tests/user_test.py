import unittest
from datetime import datetime
from Model.place import Place
from Model.user import User

"""
Testing for User which support following cases:
1.Business Rule Enforcement - Such as user uniqueness
2.User Creation Validation - Test instantiation of a User object with valid and
invalid inputs to verify constraints (e.g., email format, required fields).
3.Unique Email Constraint - Attempt to create multiple users with the same email
and ensure the model throws an exception or handles it as per the business rule.
4.Update Mechanism - Verify that updates to a user’s attributes (e.g., name) are
reflected in existing instances of the user.
"""

class TestUser(unittest.TestCase):
    
    # User uniqueness (business rule enforcement)
    def test_business_rule_enforcement(self):
        updated_at = datetime.now()
        created_at = datetime.now()
        user1 = User(id=1, updated_at=updated_at, created_at=created_at,
                      host_id="Owner", place_id="Owned place",
                      review="Great place to stay!", email="user@email.com",
                      first_name="Saul",
                      last_name="Vera")
        with self.assertRaises(ValueError):
            user2 = User(id=2, created_at=created_at, updated_at=updated_at,
                          host_id="Owner", place_id="Owned place",
                          review="Great place to stay!",
                          email=user1.email,
                          first_name="Jesse", last_name="Pinkman")

        # Test user uniqueness
        with self.assertRaises(ValueError):
            user3 = User(id=3, created_at=created_at, updated_at=updated_at,
                          host_id="Owner", place_id="Owned place",
                          review="Great place to stay!",
                          email=user1.email,
                          first_name="Mike",
                          last_name="Ehrmantraut")
            
    # Test for user creation validation
    def test_user_creation_validation(self):
        """Test user creation validation."""
        created_at = datetime.now()
        updated_at = datetime.now()
        with self.assertRaises(ValueError):
            user = User(id=1, created_at=created_at, updated_at=updated_at,
                         host_id="Owner", place_id="Owned place",
                         review="Great place to stay!",
                         email="invalid_email",
                         first_name="Lalo",
                         last_name="Salamanca")

    # Test for unique email constraint
    def test_unique_email_constraint(self):
        """Test unique email constraint."""
        
        User.users = []
        updated_at = datetime.now()
        created_at = datetime.now()
        user1 = User(id=1, updated_at=updated_at, created_at=created_at,
                      host_id="Owner", place_id="Owned place",
                      review="Great place to stay!",
                      email="user@email.com",
                      first_name="Kim",
                      last_name="Wexler")
        print("User 1 created with email:", user1.email)
        print("Existing users:", [user.email for user in User.users])
        with self.assertRaises(ValueError):
            user2 = User(id=2, created_at=created_at, updated_at=updated_at,
                          host_id="Owner", place_id="Owned place",
                          review="Great place to stay!",
                          email=user1.email,
                          first_name="Hank",
                          last_name="Schrader")

    # Update user
    def test_update_user(self):
        """Test update mechanism."""
        User.users = []
        created_at = datetime.now()
        updated_at = datetime.now()
        user = User(id=1, created_at=created_at, updated_at=updated_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!",
                     email="user@email.com",
                     first_name="Nacho",
                     last_name="Varga")
        user.first_name = "Nacho"
        self.assertEqual(user.first_name, "Nacho")
        
if __name__ == "__main__":
    unittest.main()
        