import os
import bcrypt
import mysql.connector

def add_details(user_id,password):
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    mydb = mysql.connector.connect(host='localhost',
                                   user=os.environ.get('MYSQL_USER'),
                                   passwd=os.environ.get('MYSQL_PWD'),
                                   database='rbov',
                                   auth_plugin='mysql_native_password')
    my_curr =mydb.cursor()
    my_curr.execute('insert into test (user_id,password) values (%s,%s)',(user_id,hashed))
    mydb.commit()
    mydb.disconnect()

def validate(user_id,password):
    password_bytes = password.encode('utf-8')
    mydb = mysql.connector.connect(host='localhost',
                                   user=os.environ.get('MYSQL_USER'),
                                   passwd=os.environ.get('MYSQL_PWD'),
                                   database='rbov',
                                   auth_plugin='mysql_native_password')
    my_curr = mydb.cursor()
    my_curr.execute('select password from test where user_id = %s', (user_id,))
    row = my_curr.fetchall()
    if len(row) == 1:
        hashed = row[0][0].encode('utf-8')
        if bcrypt.checkpw(password_bytes,hashed):
            print('valid user')
        else:
            print('Invalid user')
    else:
        print('user not found')

#add_details('somu@123','185176')
validate('somu@123','185176')