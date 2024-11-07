from Rbov import Rbov_class
import mysql.connector



while True:
    print('*** Welcome to Royal Bank of Vellore ***')
    print('1: Check Balance')
    print('2: Deposit money')
    print('3: Withdraw money')
    print('4: Exit')
    user_input = input("Enter your choice(1/2/3/4): ")
    if len(user_input) < 1 or len(user_input) > 1:
        print('*** Wrong input provided ***')
        exit()
    if user_input == '4':
        break
    elif user_input == '1':
        while True:
            print('*** Check balance portal ***')
            user_input_cust_id = input('Enter your CUSTOMER ID: ')
            # Basic customer id validation
            val_return = Rbov_class.cust_id_val(user_input_cust_id)
            if val_return == -1:
                print("invalid customer ID length")
                break
            else:
                # instantiate this user id
                user_input_cust_id_obj = Rbov_class(user_input_cust_id)

            # check if this customer id is present in the customer_det table
            if user_input_cust_id_obj.is_present():
                print(f'Hello Mr. {user_input_cust_id_obj.cust_lname} !!!, Below are your accounts')
                user_input_cust_id_obj.get_all_accounts(user_input_cust_id)

                break
            else:
                print('customer ID not found')
                break
    elif user_input == '2':
        print('*** Deposit money portal ***')
        user_input_cust_id = input('Enter your CUSTOMER ID: ')
        # Basic customer id validation
        val_return = Rbov_class.cust_id_val(user_input_cust_id)
        if val_return == -1:
            print("Invalid customer id")
            break
        else:
            print("valid customer proceed")
            break
    elif user_input == '3':
        print('*** Withdraw money portal ***')
        user_input_cust_id = input('Enter your CUSTOMER ID: ')
        # Basic customer id validation
        val_return = Rbov_class.cust_id_val(user_input_cust_id)
        if val_return == -1:
            print("Invalid customer id")
            break
        else:
            print("valid customer proceed")
            break
    else:
        print('*** Invalid selection ***')
