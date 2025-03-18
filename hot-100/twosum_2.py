class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            d={}
            num1=nums[i]
            num2=target-nums[i]
            if num2 in d: 
                return(d[num2],i)
            d[num1]=i
