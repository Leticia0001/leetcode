
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(k):
            if k in memo:
                return memo[k]
            if k == 0 or k == 1:
                return 1
            memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]
        return dfs(n)


sol = Solution()
print(sol.climbStairs(4))  