# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-10 14:54:05
"""
https://leetcode-cn.com/problems/binary-search/
"""

from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             m = (l + r) // 2
#             v = nums[m]
#             if v > target:
#                 r = m - 1
#             elif v < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            v = nums[m]
            if v > target:
                r = m
            elif v < target:
                l = m + 1
            else:
                return m
        return -1


func = Solution().search
print(func([-1,0,3,5,9,12], 13))
print(func([], 9))
print(func([-1, 0, 3, 5, 9, 12], 9))
print(func([-1, 0, 3, 5, 9, 12], 2))
