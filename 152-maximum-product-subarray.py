# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-18 20:46:24
@UpdateDate: 2020-05-18 21:25:01
'''
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        _max = _min = 1
        sum_max = -0xfffffff
        for x in nums:
            if x < 0:
                _max, _min = _min, _max
            _max = max(_max * x, x)
            _min = min(_min * x, x)
            sum_max = max(sum_max, _max)
        return sum_max

print(Solution().maxProduct([-2, -3, -2, -4, -10]))
