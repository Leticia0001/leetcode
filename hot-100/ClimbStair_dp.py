# Ideas: DP
# 已知走一步的方法是一種，走兩步的方法是兩種
# 從第3個開始計算直到第n個停止，將舊的值變成dp[i - 1]，並把新的值變成dp[i - 1] + dp[i - 2]
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