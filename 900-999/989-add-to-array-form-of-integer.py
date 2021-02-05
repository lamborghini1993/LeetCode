# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-22 14:47:27
"""
https://leetcode-cn.com/problems/add-to-array-form-of-integer/
"""

from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        for i in range(n - 1, -1, -1):
            t, K = K % 10, K // 10
            A[i] += t
            K += A[i] // 10
            A[i] = A[i] % 10

        while K:
            A.insert(0, K % 10)
            K = K // 10
        return A


func = Solution().addToArrayForm
print(func([1, 2, 0, 0], 34))
print(func([2, 7, 4], 181))
print(func([2, 1, 5], 806))
print(func([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1))
print(func([], 1234567))
