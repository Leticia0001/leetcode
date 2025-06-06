nums = [-1, 3, 8, -4]
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')  # 設置最初的結果為負無窮大
        for i in range(len(nums)): #外層循環，開始每個子數組
            count = 0  # 記錄當前子數組的和
            for j in range(i, len(nums)): # 內層循環，擴展子數組
                count += nums[j] # 累加當前元素
                result = max(result, count) # 更新最大和
        return result # 返回最大子數組和

solution=Solution()
print(solution.maxSubArray(nums))  # 應該輸kj出 11


