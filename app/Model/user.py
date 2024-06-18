from baseclass import BaseClass
# from ..persistence.data_manager import DataManager

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
        
        