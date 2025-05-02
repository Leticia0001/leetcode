# Ideas: DP
# There is 1 way to take one step, and 2 ways to take two steps.
# Starting from the 3rd step up to the nth, update the old value to dp[i - 1],and compute the new value as dp[i - 1] + dp[i - 2].
# Time Complexity:O(n)
# Space Complexity:O(1)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b