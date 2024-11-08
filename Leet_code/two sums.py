class Solution:
    def twoSum(self, nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                sum_of_dig = nums[i] + nums[j]
                #print(sum_of_dig)
                if sum_of_dig == target:
                    return ([i,j])
                    break


obj = Solution()
obj.twoSum([3,2,4,8,9,7,1],4)
