# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-11 15:46:24
"""
https://leetcode-cn.com/problems/squares-of-a-sorted-array/
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """双指针，从两边到中间，更优雅"""
        n = len(nums)
        i, j, k = 0, n - 1, n - 1
        ans = [0] * n
        while i <= j:
            a = nums[i] ** 2
            b = nums[j] ** 2
            if a > b:
                ans[k] = a
                i += 1
            else:
                ans[k] = b
                j -= 1
            k -= 1
        return ans

    def sortedSquares_2(self, nums: List[int]) -> List[int]:
        """双指针，从中间到两边，不优雅"""
        result = []
        start = -1
        for i, v in enumerate(nums):
            if v < 0:
                start = i
            nums[i] = v * v
        i, j, n = start, start + 1, len(nums)
        while i >= 0 or j < n:
            if i < 0:
                result.append(nums[j])
                j += 1
            elif j >= n:
                result.append(nums[i])
                i -= 1
            else:
                if nums[i] > nums[j]:
                    result.append(nums[j])
                    j += 1
                else:
                    result.append(nums[i])
                    i -= 1

        return result


func = Solution().sortedSquares
print(func([-4, -4, -1]))
print(func([-4, -1, 0]))
print(func([-4, -1, 0, 3, 10]))
print(func([0, 3, 10]))
print(func([1, 3, 10]))
print(func([-17, -3, 2, 3, 11]))
