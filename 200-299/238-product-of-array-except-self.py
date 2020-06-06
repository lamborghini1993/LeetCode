# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-04 16:44:44
@Description: https://leetcode-cn.com/problems/product-of-array-except-self/
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur_end = []
        tmp = 1
        for num in reversed(nums):
            tmp *= num
            cur_end.insert(0, tmp)
        cur_end.append(1)
        tmp = 1
        result = []
        for i, num in enumerate(nums):
            result.append(tmp * cur_end[i+1])
            tmp *= num
        return result


func = Solution().productExceptSelf
print(func([1, 10]))
print(func([1, 2, 3, 4]))
