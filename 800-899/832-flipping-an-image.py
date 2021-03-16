# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-02-24 10:45:02
"""
https://leetcode-cn.com/problems/flipping-an-image/
"""

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for lst in A:
            N = len(lst)
            for i in range((N + 1) // 2):
                j = N - i - 1
                if i == j:
                    lst[i] = 1 - lst[i]
                    continue
                lst[i], lst[j] = 1 - lst[j], 1 - lst[i]
        return A


func = Solution().flipAndInvertImage
print(func([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(func([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
print(func([[1], [1, 0], [0, 1, 1], [1, 0, 1, 0]]))
