# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-05-27 19:13:10
@UpdateDate: 2020-05-27 19:37:33
@Description: 
https://leetcode-cn.com/problems/house-robber/
'''

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        dp = [0 for _ in nums]
        dp.append(0)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            # 只保存两个状态，可进一步做空间优化
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[len(nums)]

func = Solution().rob
print(func([1, 2, 3, 1]))
print(func([2, 7, 9, 3, 1]))
print(func([1, 2, 3, 13, 4, 1, 5, 6, 7, 87]))
