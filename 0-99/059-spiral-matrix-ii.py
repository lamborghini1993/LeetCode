# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-03-16 16:59:13
"""
https://leetcode-cn.com/problems/spiral-matrix-ii/
"""


# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-03-15 14:01:55
"""
https://leetcode-cn.com/problems/spiral-matrix/
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        vis = [[0] * n for x in range(n)]
        i = j = 0
        vis[i][j] = 1
        cnt = 1
        while True:
            add = False
            for (tx, ty) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                while True:
                    a, b = i + tx, j + ty
                    if a < 0 or a >= n or b < 0 or b >= n:
                        break
                    if vis[a][b]:
                        break
                    i, j = a, b
                    cnt += 1
                    vis[i][j] = cnt
                    add = True
            if not add:
                return vis


func = Solution().generateMatrix
print(func(1))
print(func(2))
print(func(3))
