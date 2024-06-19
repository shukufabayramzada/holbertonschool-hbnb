from Model.baseclass import BaseClass
from Persistence.data_manager import DataManager

class User(BaseClass):
    
    users = []
    
    def __init__(self, id, email, first_name, last_name, created_at, updated_at):
        super.__init__(id, created_at, updated_at)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        
    @staticmethod
    def user_check(user_instance):
        if user_instance not in User.users:
            User.users.append(user_instance)
            
    @staticmethod
    def email_check(email):
        data_manager = DataManager()
        all_users = data_manager.get_all('User')
        return any(user['email'] == email for user in all_users)
    
    
    def not_own_review(self, host_id, place_id, review):
        self.host_id = host_id
        self.place_id = place_id
        self.review = review
        
        if host_id == place_id:
            raise ValueError("Owners can`t review their own places")
        
        