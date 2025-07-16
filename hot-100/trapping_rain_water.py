# This algorithm calculates the amount of trapped rainwater between bars of varying height using the two-pointer technique.
# It keeps track of the maximum height from the left and right, and iteratively accumulates water trapped at each position.
# Time Complexity: O(n) - each bar is visited at most once.
# Space Complexity: O(1) - only constant extra space is used.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += max(0, right_max - height[right])

        return total_water

        