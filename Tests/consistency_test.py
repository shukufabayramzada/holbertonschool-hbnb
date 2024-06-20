#!/usr/bin/python3
import unittest
from datetime import datetime
from Model.user import User


"""
Test support Consistency Checks - test that the created_at and 
updated_at fields are automatically set on creation and update operations.
"""

class TestConsistency(unittest.TestCase):
    def test_consistency_checks(self):
        """Test consistency checks."""
        User.users = []
        updated_at = datetime.now()
        created_at = datetime.now()
        user = User(id=1, updated_at=updated_at, created_at=created_at,
                     host_id="Owner", place_id="Owned place",
                     review="Great place to stay!",
                     email="user@email.com",
                     first_name="Nelly", last_name="Sierra")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

if __name__ == '__main__':
    unittest.main()