# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-26 14:17:55
"""
https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/
"""

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        result = [0] * 100
        ret = 0
        for (x, y) in dominoes:
            t = x * 10 + y if x < y else y * 10 + x
            ret += result[t]
            result[t] += 1
        return ret


func = Solution().numEquivDominoPairs
print(func([[0, 1], [0, 1], [0, 1]]))
