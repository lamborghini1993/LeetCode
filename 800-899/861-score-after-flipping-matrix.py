# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-07 17:34:15
"""
https://leetcode-cn.com/problems/score-after-flipping-matrix/
"""

from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        rowN, colN = len(A), len(A[0])
        for rows in A:
            if rows[0]:
                continue
            for i, x in enumerate(rows):
                rows[i] = 1 - x
        result = rowN * (2**(colN - 1))
        for col in range(1, colN):
            one_num = 0
            for row in range(rowN):
                if A[row][col]:
                    one_num += 1
            result += max(one_num, rowN - one_num) * (2**(colN - col - 1))
        return result


func = Solution().matrixScore
print(func([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
print(func([[0], [1], [0]]))
