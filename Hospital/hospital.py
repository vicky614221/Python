#This hospital has mainly 3 ways to interact
# 1. Patient portal
# 2. Staff portal
# 3. Admin portal
import tkinter.messagebox

import mysql.connector
import os

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

    def get_portal_user_info(self,user,user_id):
        # inquire table(based on user)
        try:
            mydb = mysql.connector.connect(host='localhost',user=os.environ.get('MYSQL_USER'),passwd=os.environ.get('MYSQL_PWD'),database='rbov',auth_plugin='mysql_native_password')
            my_curr = mydb.cursor()
            if user == 'P':
                my_curr.execute('select * from patient where user_id = %s', (user_id,))
                row = my_curr.fetchall()
        except:
            tkinter.messagebox.showinfo(title='Database error',message='failed connecting to Database')
    def update_portal_user_info(self,user):
        # update query to update portal user details
        pass

    def add_portal_user(self,user):
        # insert query to insert portal user details
        pass

    def delete_portal_user(self,user):
        # delete query to delete portal user
        pass
