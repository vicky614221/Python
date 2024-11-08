from Rbov import Rbov_class
import mysql.connector
while True:
    print('*** Welcome to Royal Bank of Vellore ***')
    print('1: Check Balance')
    print('2: Deposit money')
    print('3: Withdraw money')
    print('4: Add New Customer')
    print('5: Exit')
    user_input = input("Enter your choice(1/2/3/4/5): ")
    if len(user_input) < 1 or len(user_input) > 1:
        print('*** Wrong input provided ***')
        exit()
    if user_input == '5':
        break
    elif user_input == '1':
        while True:
            print('*** Check balance amount portal ***')
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
    elif user_input == '4':
        print('*** Add customer portal ***')
        user_input_cust_id = input('Enter your CUSTOMER ID(Max length is 32): ')
        # Basic customer id validation
        val_return = Rbov_class.cust_id_val(user_input_cust_id)
        if val_return != -1:
            user_input_fname = input('Please enter your first name(Max length is 50):')
            if len(user_input_fname) > 0 and len(user_input_fname) <= 32:
                user_input_lname = input('Please enter your last name(Max length is 50): ')
                if len(user_input_lname) > 0 and len(user_input_lname) <= 32:
                    user_input_email = input('Please enter your email id( Max length is 80): ')
                    if len(user_input_email) > 0 and len(user_input_email) <= 80:
                        ### OBJECT CREATION ###
                        user_input_cust_id_obj = Rbov_class(user_input_cust_id)
                        ### OBJECT CREATION END ###
                        if user_input_cust_id_obj.is_present():
                            print('You already are part of Royal bank of vellore')
                        else:
                            user_input_cust_id_obj.add_customer(user_input_cust_id,user_input_fname,user_input_lname,user_input_email)
                            print(f'Hello Mr. {user_input_lname[0].upper()}{user_input_lname[1:len(user_input_lname)].lower()} !!!, Thanks for joining')

                            while True:
                                user_wish_to_op_acct = input('Would you like to open an account with us? (Y-yes/N-No): ')
                                if user_wish_to_op_acct == ('n' or 'N'):
                                    print('We would request you to open an account within 7 days if not opened already after which the customer ID will be removed')
                                    break
                                elif user_wish_to_op_acct == ('y' or 'Y'):
                                    print('Below are the account types that you are eligible to open ')
                                    print('1) Savings account')
                                    print('2) Credit card account')
                                    print('3) Debit card account')
                                    user_accnt_sel = input("Select your option: ")
                                    if user_accnt_sel == '1':
                                        user_input_cust_id_obj.add_account(user_input_cust_id,'PER')
                                    elif user_accnt_sel == ('2' or '3'):
                                        print('feature under maintenance')
                                        break
                                    else:
                                        print("Invalid option selected, try again")

                                else:
                                    print('Invalid option selected')

                    else:
                        print('Invalid email id provided!!!')
                else:
                    print('Invalid last name provided!!!')
            else:
                print('Invalid first name provided!!!')
        else:
            print('Invalid customer id provided!!!')

    else:
        print('*** Invalid selection ***')
