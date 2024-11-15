from random import randint

import mysql.connector
import random
class Rbov_class:
    def __init__(self,user_input_cust_id,pass_word):
        self.cust_id = user_input_cust_id
        self.cust_pwd = pass_word

    def is_present(self):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="vicky",database="rbov",auth_plugin='mysql_native_password')
        if mydb.is_connected():
            my_cursor_cust_det = mydb.cursor()
            value_id = (self.cust_id,self.cust_pwd)
            #value_pwd = (,)
            my_cursor_cust_det.execute("select * from customer_det where cust_id = %s and pass_word = %s", value_id)
            rows = my_cursor_cust_det.fetchall()
            if len(rows) == 1:
                for row in rows:
                    self.cust_fname = row[1]
                    self.cust_lname = row[2]
                    self.cust_email = row[3]
                 #   self.cust_pwd = row[4]
                    return True
        else:
            print('Error in connecting DB')
            return False
        my_cursor_cust_det.close()
        mydb.close()

    def get_all_accounts(self,cust_id):
        mydb = mysql.connector.connect(host='localhost',user='root',passwd='vicky',database='rbov',auth_plugin='mysql_native_password')
        my_cursor_get_bal = mydb.cursor()
        value = (cust_id,)
        my_cursor_get_bal.execute("select * from customer_acct where cust_id = %s",value)
        query_result = my_cursor_get_bal.fetchall()
        my_cursor_get_bal.close()
        mydb.close()
        while True:
            if len(query_result) > 0:
                i=0
                for row in query_result:
                    i=i+1
                    print(f" {i})Account type:  {row[1]} || Account product:  {row[2]}  || Account number:  {row[3]}")
                user_input_acct = input('Select which account balance you wish to see: ')
                if len(user_input_acct) == 0:
                    print("invalid account option choosen, try again")
                else:
                    try:
                        user_input_acct_int = int(user_input_acct)
                    except:
                        print("*** ENTER NUMERIC VALUE PLEASE")
                        break
                    if len(user_input_acct) == 0 or user_input_acct_int <=0 or user_input_acct_int > i:
                        print("invalid account option choosen, try again")
                    else:
                        #selected_account = tuple()
                        selected_account = query_result[user_input_acct_int-1]
                        print("*** SELECTED ACCOUNT ***")
                        print(f"Account type:  {selected_account[1]} || Account product:  {selected_account[2]} "
                              f" || Account number:  {selected_account[3]}")
                        print(f"*** Account balance *** ")
                        print(f"Rs. {selected_account[4]}")
                        break
            else:
                print('No accounts found')
                break
    def add_customer(self,cust_id, cust_fname, cust_lname, cust_email):
        self.cust_id = cust_id
        self.cust_fname = cust_fname
        self.cust_lname = cust_lname
        self.cust_email = cust_email

        mydb = mysql.connector.connect(host='localhost',user='root',passwd='vicky',database='rbov',auth_plugin='mysql_native_password')
        my_cursor = mydb.cursor()
        value=(self.cust_id.lower(),self.cust_fname.upper(),self.cust_lname.upper(),self.cust_email.lower())
        my_cursor.execute("insert into  customer_det values (%s,%s,%s,%s)",value)
        mydb.commit()
        my_cursor.close()
        mydb.close()

    def add_account(self,cust_id,acct_prod):
        self.cust_id = cust_id
        self.acct_prod = acct_prod

        mydb = mysql.connector.connect(host='localhost',user='root',passwd='vicky',database='rbov',auth_plugin='mysql_native_password')
        my_cursor = mydb.cursor()
        acct_no = 'RBOVPER' + str(randint(10000,99999))
        value=(self.cust_id,self.acct_prod,'0001',acct_no,0)
        print(value)
        my_cursor.execute("insert into customer_acct values (%s,%s,%s,%s,%s)", value)
        mydb.commit()
        my_cursor.close()
        mydb.close()

    @staticmethod
    def cust_id_val(user_input_cust_id):
        if len(user_input_cust_id) == 0 or len(user_input_cust_id) > 32:
            return -1
