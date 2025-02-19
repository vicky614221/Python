class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        cf = str()
        for i in range(len(strs)):
            for j in range(len(strs) - i - 1):
                if len(strs[j]) > len(strs[j + 1]):
                    temp = strs[j]
                    strs[j] = strs[j + 1]
                    strs[j + 1] = temp
        if len(strs) > 1:
            SmallestWord = strs.pop(0)
            SmallestWordLength = len(SmallestWord)
            CommonPrefixFound = True
            CommonPrefix = str()
            CommonPrefixList = list()
            for i in range(SmallestWordLength):
                for j in range(len(strs)):
                    if SmallestWord[i] == strs[j][i]:
                        CommonPrefix = CommonPrefix + SmallestWord[i]
                    else:
                        CommonPrefixFound = False
                        break
                if CommonPrefixFound:
                    CommonPrefixList.append(CommonPrefix)
                    CommonPrefix = ''
                else:
                    break
            if len(CommonPrefixList) > 0:
                for i in (CommonPrefixList):
                    cf = cf + i[0]
                return(cf)
            else:
                return cf
        elif len(strs) == 1:
            cf = strs[0]
            return cf
        else:
            return cf



str1 = Solution()
str1.longestCommonPrefix(["sd","flow","flight"])