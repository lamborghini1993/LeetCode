# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-01 10:38:48
@Description: https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/
'''

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        result = [(x + extraCandies >= max_num) for x in candies]
        return result
