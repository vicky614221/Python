class Solution:
    def romanToInt(self, s: str):
        sub = 0
        rom_sym_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        rom_sym_subtr = (('IV',-2),('IX',-2),('XL',-20),('XC',-20),('CD',-200),('CM',-200))
        for k,v in rom_sym_subtr:
            if s.rfind(k) > -1:
                sub = v + sub
        print(sub)
        sum = 0
        for letter in s:
            rom_sym_val.__contains__(letter)
            sum = (rom_sym_val.get(letter)) + sum

        return (sum + sub)
obj = Solution()
obj.romanToInt('MCDLXXVI')