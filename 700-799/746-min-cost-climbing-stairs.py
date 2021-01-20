# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-21 16:03:50
"""
https://leetcode-cn.com/problems/min-cost-climbing-stairs/
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            cur = min(first, second) + cost[i]
            first, second = second, cur
        return min(first, second)


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         dp = [0] * len(cost)
#         for i, v in enumerate(cost):
#             if i in (0, 1):
#                 dp[i] = v
#                 continue
#             dp[i] = min(dp[i - 2], dp[i - 1]) + v
#         return min(dp[-1], dp[-2])

func = Solution().minCostClimbingStairs
print(func([10, 15, 20]))
print(func([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
