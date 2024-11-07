import mysql.connector


class Rbov_class:
    def __init__(self):
        self.cust_id = self
        self.cust_bal = None
        self.cust_name = None

    def is_present(self):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="vicky",database="rbov")
        if mydb.is_connected():
            print('Connected to database ' + mysql.connector.database)
        my_cursor = mydb.cursor()
        my_cursor.execute("select cust_id from customer_det where cust_id = '%s'", self)

        query_result = my_cursor.fetchone()
        if query_result == self:
            return True
        else:
            return False
    def get_cust_bal(self):
        if self.cust_bal is None:
            return '*'
        else:
            return self.cust_bal
    def get_cust_name(self):
        if self.cust_name is None:
            return '*'
        else:
            return self.cust_name

    @staticmethod
    def cust_id_val(user_input_cust_id):
        if len(user_input_cust_id) == 0 or len(user_input_cust_id) > 32:
            return -1
