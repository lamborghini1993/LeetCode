# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-05-28 19:35:49
@Description: 
https://leetcode-cn.com/problems/longest-increasing-subsequence/
'''

from typing import List


# ? 动规
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [0 for _ in range(len(nums) + 1)]
#         result = 0
#         for i in range(1, len(nums) + 1):
#             dp[i] = 1
#             for j in range(1, i):
#                 if nums[j - 1] < nums[i - 1]:
#                     dp[i] = max(dp[j] + 1, dp[i])
#             result = max(result, dp[i])
#         return result


# ? 贪心 + 二分
class Solution:
    def _find_record(self, record: List[int], n: int):
        if not record:
            record.append(n)
            return
        if record[-1] < n:
            record.append(n)
            return
        l, r = 0, len(record)
        while l < r:
            m = (l + r) // 2
            if record[m] < n:
                l = m + 1
            else:
                r = m
        record[l] = n

    def lengthOfLIS(self, nums: List[int]) -> int:
        record = []
        for num in nums:
            self._find_record(record, num)
        return len(record)

func = Solution().lengthOfLIS
print(func([10, 9, 2, 5, 3, 7, 101, 18]))
print(func([10, 9, 2, 5, 1, 2, 3, 7]))
print(func([]))
print(func([2, 1]))
print(func([1, 3, 6, 7, 9, 4, 10, 5, 6]))
