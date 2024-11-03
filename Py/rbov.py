class rbov_class:
    def __init__(self,cust_id):
        self.cust_id = cust_id
        self.cust_bal = None
        self.cust_name = None
        file_cust_det = dict()
        fhand_cust_file = open('RBOV_customer_id_list.txt')
        for each_line in fhand_cust_file:
            each_line = each_line.strip()
            each_line_word = each_line.split()
            if len(each_line_word) == 3:
                if each_line_word[0] == self.cust_id:
    #                self.cust_id = each_line_word[0]
                    self.cust_bal = each_line_word[1]
                    self.cust_name = each_line_word[2]
                    break
            else:
                print('Incorrect file data, check file')
                break
    def get_cust_bal(self):
        if self.cust_bal == None:
            return '*'
        else:
            return self.cust_bal
    def get_cust_name(self):
        if self.cust_name == None:
            return '*'
        else:
            return self.cust_name

    @staticmethod
    def cust_id_val(user_input_cust_id):
        if len(user_input_cust_id) != 8:
            return -1
