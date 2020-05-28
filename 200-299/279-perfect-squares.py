# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-05-28 17:13:41
@Description: 
    https://leetcode-cn.com/problems/perfect-squares/
'''

# ?动态规划
# class Solution:
#     def numSquares(self, n: int) -> int:
#         # w = [i * i for i in range(1, n) if i * i <= n else break]
#         w = []
#         for i in range(1, n + 1):
#             t = i * i
#             if t > n:
#                 break
#             w.append(t)
#         dp = [0] * (n + 1)
#         for i in range(1, n + 1):
#             for v in w:
#                 if i < v:
#                     break
#                 if dp[i]:
#                     dp[i] = min(dp[i - v] + 1, dp[i])
#                 else:
#                     dp[i] = dp[i - v] + 1
#         return dp[n]


class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        if self.isSquares(n):
            return 1
        for i in range(1, n):
            t = n - i * i
            if t < 0:
                return 3
            if self.isSquares(t):
                return 2

    def isSquares(self, n: int) -> bool:
        for i in range(1, n + 1):
            t = i * i
            if t == n:
                return True
            if t > n:
                return False

func = Solution().numSquares
for i in range(1, 100):
    print(f"f[{i}] = {func(i)}")
