# Runtime: 49 ms
# Memory: 28.46 MB
#
# Time Complexity: O(n)
#   - n: number of height bars
#   - Each bar is visited at most once by either the left or right pointer
#   - Total iterations are linear: O(n)
#
# Space Complexity: O(1)
#   - Only a constant amount of extra space is used for variables
#   - No additional data structures grow with input size
#
# Key Idea:
# 1. Use two pointers, starting from both ends of the array
# 2. Calculate the area between the two pointers based on the shorter height
# 3. Move the pointer with the shorter height inward to potentially find a larger area
# 4. Repeat until the two pointers meet, tracking the maximum area found


class Solution:
    def maxArea(self, height: List[int]) -> int:
        index_low = 0
        index_high = len(height) - 1
        max_area = 0

        # Loop until the two pointers meet
        while index_low < index_high:
            distance = index_high - index_low
            # Calculate area using the shorter line
            if height[index_low] < height[index_high]:
                now_area = height[index_low] * distance
                index_low += 1  # Move the left pointer inward
            else:
                now_area = height[index_high] * distance
                index_high -= 1  # Move the right pointer inward

            # Update max_area if a larger area is found
            if now_area > max_area:
                max_area = now_area

        return max_area
