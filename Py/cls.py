from rbov import rbov_class



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
            val_return = rbov_class.cust_id_val(user_input_cust_id)
            if val_return == -1:
                print("Invalid customer id")
                break
            else:
                # Check RBOV customer list file for this customer id
                user_input_cust_id_obj = rbov_class(user_input_cust_id)
                bal=user_input_cust_id_obj.get_cust_bal()
                if bal == '*':
                    print('No data found')
                    break
                name = user_input_cust_id_obj.get_cust_name()
                print(f'Hello {name}, your ID {user_input_cust_id} has balance of ${bal}')
                break
    elif user_input == '2':
        print('*** Deposit money portal ***')
        user_input_cust_id = input('Enter your CUSTOMER ID: ')
        # Basic customer id validation
        val_return = cust_id_val(user_input_cust_id)
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
        val_return = cust_id_val(user_input_cust_id)
        if val_return == -1:
            print("Invalid customer id")
            break
        else:
            print("valid customer proceed")
            break
    else:
        print('*** Invalid selection ***')
