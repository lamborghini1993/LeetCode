# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-11-19 11:34:54
"""
https://leetcode-cn.com/problems/move-zeroes/
"""

from typing import List


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(len(nums)):
#             if nums[i]:
#                 continue
#             for j in range(i + 1, len(nums)):
#                 if nums[j]:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     break


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rec = 0
        for i, value in enumerate(nums):
            if value:
                nums[rec] = value
                rec += 1
        for i in range(rec, len(nums)):
            nums[i] = 0


func = Solution().moveZeroes
t = [0, 1, 0, 3, 12]
func(t)
print(t)
