# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-02-22 15:20:44
"""
https://leetcode-cn.com/problems/toeplitz-matrix/
"""

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for col in range(n - 1):
            cnt = matrix[0][col]
            x, y = 1, col + 1
            while x < m and y < n:
                if matrix[x][y] != cnt:
                    return False
                x += 1
                y += 1

        for row in range(1, m - 1):
            cnt = matrix[row][0]
            x, y = row + 1, 1
            while x < m and y < n:
                if matrix[x][y] != cnt:
                    return False
                x += 1
                y += 1

        return True


func = Solution().isToeplitzMatrix
print(func([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(func([[1, 2], [2, 2]]))
