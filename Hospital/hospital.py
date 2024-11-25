#This hospital has mainly 3 ways to interact
# 1. Patient portal
# 2. Staff portal
# 3. Admin portal
import tkinter.messagebox
import string
import random
import mysql.connector
import os
import bcrypt

from mysql.connector import connect


class Hospital:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch

class PortalUser(Hospital):
    def __init__(self, user, id, name, dob, gender,email,phone_no,aadhar,address):
        self.user = user
        self.user_id = id
        self.user_name = name
        self.user_dob = dob
        self.user_gender = gender
        self.user_email = email
        self.user_phone_no = phone_no
        self.user_aadhar = aadhar
        self.user_address = address

    def is_valid_user(self,user,user_id,password):
        password_bytes = password.encode('utf-8')
        mydb = mysql.connector.connect(host='localhost',user=os.environ.get('MYSQL_USER'),passwd=os.environ.get('MYSQL_PWD'),database='rbov',auth_plugin='mysql_native_password')
        my_curr = mydb.cursor()
        if user == 'P':
            my_curr.execute('select patient_log_pwd from patient where patient_id = %s',(user_id,))
            row = my_curr.fetchall()
            if len(row) == 1:
                password_db = (row[0][0]).encode('utf-8')
                if bcrypt.checkpw(password_bytes,password_db):
                    my_curr.execute('select * from patient where patient_id = %s', (user_id,))
                    return  True
                else:
                    tkinter.messagebox.showinfo(title='Error',message='Incorrect password')
            else:
                tkinter.messagebox.showinfo(title='Error',message='Incorrect details')


    def get_portal_user_info(self):
        # inquire table(based on user)
        mydb = mysql.connector.connect(host='localhost',user=os.environ.get('MYSQL_USER'),passwd=os.environ.get('MYSQL_PWD'),database='rbov',auth_plugin='mysql_native_password')
        my_curr = mydb.cursor()
        if self.user == 'P':
            #my_curr.execute('select * from patient where patient_id = %s', (self.user_id,))
            my_curr.execute('select p.patient_id,patient_name,patient_dob,patient_gender,patient_email,patient_phone_no,aadhar_no,patient_address,appointment_id,appointment_date,appointment_time,appointment_doctor_id,appointment_doctor_name from patient p inner join appointment a on p.patient_id = a.patient_id where a.patient_id = %s',(self.user_id,))
            row = my_curr.fetchall()
            if len(row)>1:
                return row

        #else:
            #tkinter.messagebox.showinfo(title='Database error',message='failed connecting to Database')
    def update_portal_user_info(self,user,**data):
        # update query to update portal user details
        if user == 'P':
            data.keys()
            print(data)
            mydb = mysql.connector.connect(host='localhost',user=os.environ.get('MYSQL_USER'),passwd=os.environ.get('MYSQL_PWD'),database='rbov',auth_plugin='mysql_native_password')
            my_curr = mydb.cursor()
    def add_portal_user(self,user,**data):
        # insert query to insert portal user details
        if user == 'P':
            user_id = 'PA' + str(random.randint(10000000,99999999))
            characters = string.ascii_letters + string.digits
            password_temp = ''.join(random.choices(characters,k=10))
            hashed_pwd = bcrypt.hashpw(password_temp.encode('utf-8'),bcrypt.gensalt())
            mydb = mysql.connector.connect(host='localhost', user=os.environ.get('MYSQL_USER'),
                                           passwd=os.environ.get('MYSQL_PWD'), database='rbov',
                                           auth_plugin='mysql_native_password')
            my_curr = mydb.cursor()
            my_curr.execute('insert into patient (patient_id,patient_log_pwd,patient_name,patient_dob,patient_gender,patient_email,patient_phone_no,aadhar_no,patient_address) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                                        , (user_id, hashed_pwd,
                                                           data.get('patient_name'),data.get('patient_dob'),
                                                           data.get('patient_gen'),data.get('patient_email'),
                                                           data.get('patient_phone'),data.get('patient_adhar'),
                                                           data.get('patient_addr')))
            mydb.commit()
            tkinter.messagebox.showinfo(title='!!! PATIENT ADDED !!!',message=f'Your patient id is: {user_id} and temporary password is: '
                                                                              f'{password_temp}')
            return True

    def delete_portal_user(self,user):
        # delete query to delete portal user
        pass
