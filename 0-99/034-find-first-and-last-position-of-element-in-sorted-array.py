# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-01 16:24:52
"""
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1, -1
        N = len(nums)

        def find(left=True):
            l, r = 0, N - 1
            while l < r:

                t = l + r
                if not left:
                    t += 1
                m = t // 2

                if target < nums[m]:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    if left:
                        r = m
                    else:
                        l = m
            return l

        left = find(True)
        if nums[left] != target:
            return -1, -1
        right = find(False)
        return left, right


func = Solution().searchRange
print(func([5, 7, 7, 8, 8, 10], 10))
print(func([5, 7, 7, 8, 8, 10], 9))
print(func([5, 7, 7, 8, 8, 10], 8))
print(func([5, 7, 7, 8, 8, 10], 7))
print(func([5, 7, 7, 8, 8, 10], 5))

print(func([5, 7], 7))
print(func([5], 5))
print(func([], 5))

