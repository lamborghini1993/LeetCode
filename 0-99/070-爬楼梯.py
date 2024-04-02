#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# @lc code=end

print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(10))