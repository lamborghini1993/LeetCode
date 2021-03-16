# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-03-15 14:01:55
"""
https://leetcode-cn.com/problems/spiral-matrix/
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        N, M = len(matrix), len(matrix[0])
        vis = [[0] * M for x in range(N)]
        i = j = 0
        vis[i][j] = 1
        result.append(matrix[i][j])
        while True:
            add = False
            for (tx, ty) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                while True:
                    a, b = i + tx, j + ty
                    if a < 0 or a >= N or b < 0 or b >= M:
                        break
                    if vis[a][b]:
                        break
                    i, j = a, b
                    vis[i][j] = 1
                    result.append(matrix[i][j])
                    add = True
            if not add:
                return result


func = Solution().spiralOrder
print(func([[1]]))
print(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(func([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
