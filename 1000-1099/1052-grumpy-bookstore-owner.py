# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-02-23 13:56:59
"""
https://leetcode-cn.com/problems/grumpy-bookstore-owner/
"""

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        max_add = 0
        for i in range(X):
            if grumpy[i]:
                max_add += customers[i]

        tmp_add = max_add
        for i in range(X, len(customers)):
            if grumpy[i]:
                tmp_add += customers[i]
            if grumpy[i - X]:
                tmp_add -= customers[i - X]
            max_add = max(tmp_add, max_add)
        
        for i,v in enumerate(customers):
            if not grumpy[i]:
                max_add += v

        return max_add


func = Solution().maxSatisfied
print(func([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
