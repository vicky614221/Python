class Solution:

    def isPalindrome(self, x: int):
        int_str = str(x)
        int_str_tup = int_str
        #print(int_str_tup)
        int_str_list = list()
        for each_dig in range(0,len(int_str)):
            int_str_list.append(int_str[each_dig])
        #print(int_str_list)
        int_str_rev = list()
        for each_digit_ind in range(len(int_str)-1,-1,-1):
            int_str_rev.append(int_str[each_digit_ind])
        #print(int_str_rev)

        if int_str_list == int_str_rev:
            return True
        else:
            return False


obj = Solution()
obj.isPalindrome(98989)
