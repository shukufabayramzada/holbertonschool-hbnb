from Model.baseclass import BaseClass
from Persistence.data_manager import DataManager
import re

class User(BaseClass):
    
    users = []
    
    def __init__(self, email, first_name, last_name, host_id, place_id, reviews, created_at=None, updated_at=None, id=None):
        if id:
            self.id = id
        else:
            super().__init__()  # Generate new UUID only if ID is not provided
        
        if created_at:
            self.created_at = created_at
        if updated_at:
            self.updated_at = updated_at
        
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address")
        
        if self.email_check(email):
            raise ValueError("Email address already in use")
        
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.host_id = host_id
        self.place_id = place_id
        self.reviews = []
        
        User.users.append(self)
        
    @staticmethod
    def user_check(user_instance):
        if user_instance not in User.users:
            User.users.append(user_instance)
            
    @staticmethod
    def email_check(email):
        if any(user.email == email for user in User.users):
            return True
    
    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
    
    def not_own_review(self, host_id, place_id, review):
        self.host_id = host_id
        self.place_id = place_id
        self.reviews = []
        
        if host_id == place_id:
            raise ValueError("Owners can`t review their own places")
        
        