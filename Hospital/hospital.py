#This hospital has mainly 3 ways to interact
# 1. Patient portal
# 2. Staff portal
# 3. Admin portal
class Hospital:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch

class PortalUser(Hospital):
    def __init__(self, user, id, name, age, gender):
        self.user = user
        self.patient_id = id
        self.patient_name = name
        self.patient_age = age
        self.patient_gender = gender

    def get_portal_user_info(self,user):
        # inquire table(based on user)
        pass

    def update_portal_user_info(self,user):
        # update query to update portal user details
        pass

    def add_portal_user(self,user):
        # insert query to insert portal user details
        pass

    def delete_portal_user(self,user):
        # delete query to delete portal user
        pass
