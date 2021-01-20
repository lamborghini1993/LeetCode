# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-20 10:10:15
"""
https://leetcode-cn.com/problems/maximum-product-of-three-numbers/
"""

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return nums[1] * nums[2] * nums[0]

        min_lst = sorted([x for x in nums if x < 0])
        max_lst = sorted([x for x in nums if x >= 0], reverse=True)
        if not max_lst:
            return min_lst[-1] * min_lst[-2] * min_lst[-3]

        if len(min_lst) >= 2:
            a = min_lst[0] * min_lst[1] * max_lst[0]
            if len(max_lst) >= 3:
                a = max(a, max_lst[0] * max_lst[1] * max_lst[2])
            return a

        return max_lst[0] * max_lst[1] * max_lst[2]


func = Solution().maximumProduct
print(func([-10, -20]))
print(func([-10, 4, 6, 1, 0]))
print(func([-10, -4, -6, -1, 0]))
print(func([-10, -4, -6, -1]))
print(func([1, 2, 3]))
print(func([1, 2, 3, 4]))
print(func([1, 2, -3, 4]))
print(func([1, 2, -3, -4]))
