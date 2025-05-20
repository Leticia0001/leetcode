#Time Complexity:O(n)
#Space Complexity:O(n)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length

        # prefix
        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]

        # suffix
        suffix = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
