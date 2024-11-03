user_input1 = input("enter first number: ")
user_input2 = input("enter second number: ")


try:
    user_input1_int = int(user_input1)
except:
    print("enter 1st numeric value")
    exit()

try:
    user_input2_int = int(user_input2)
except:
    print("enter 2nd numeric value")
    exit()

print(user_input1_int + user_input2_int)


#i = 1
