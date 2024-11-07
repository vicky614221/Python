import mysql.connector

from Py.check_sql import my_cursor, value, query_result


class Rbov_class:
    def __init__(self,user_input_cust_id):
        self.cust_id = user_input_cust_id

    def is_present(self):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="vicky",database="rbov",auth_plugin='mysql_native_password')
        if mydb.is_connected():
            my_cursor_cust_det = mydb.cursor()
            value = (self.cust_id,)
            my_cursor_cust_det.execute("select * from customer_det where cust_id = %s", value)
            [(row)] = my_cursor_cust_det.fetchall()
            if len(row) > 0:
                self.cust_fname = row[1]
                self.cust_lname = row[2]
                self.cust_email = row[3]
                return True
        else:
            print('Error in connecting DB')

    def get_all_accounts(self,cust_id):
        mydb = mysql.connector.connect(host='localhost',user='root',passwd='vicky',database='rbov',auth_plugin='mysql_native_password')
        my_cursor_get_bal = mydb.cursor()
        value = (cust_id,)
        my_cursor_get_bal.execute("select * from customer_acct where cust_id = %s",value)
        query_result = my_cursor_get_bal.fetchall()
        if len(query_result) > 0:
            i=0
            for row in query_result:
                i=i+1
                print(f" {i})Account type:  {row[1]} || Account product:  {row[2]}  || Account number:  {row[3]}")


        else:
            print('No accounts found')
    @staticmethod
    def cust_id_val(user_input_cust_id):
        if len(user_input_cust_id) == 0 or len(user_input_cust_id) > 32:
            return -1
