#Time Complexity:O(n)
#Space Complexity:O(n)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) #make sure the length of the input 
        output = [1] * length #default output=[1,1,1,1]

        # prefix
        prefix = 1 #default prefix=1 
        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]

        # suffix
        suffix = 1 #default suffix=1
        for i in range(length - 1, -1, -1): #range(start, stop, step)
            output[i] *= suffix
            suffix *= nums[i]

        return output
