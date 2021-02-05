# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-29 17:50:13
"""
https://leetcode-cn.com/problems/path-with-minimum-effort/
"""

from queue import PriorityQueue
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        N, M = len(heights), len(heights[0])
        direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def in_range(x, y):
            if x < 0 or x >= N:
                return False
            if y < 0 or y >= M:
                return False
            return True

        def is_end(x, y):
            if x == N - 1 and y == M - 1:
                return True
            return False

        queue = PriorityQueue()
        queue.put((0, (0, 0)))
        visit = {}
        edge = {}
        visit[(0, 0)] = 0
        while queue:
            t, info = queue.get()
            x, y = info
            if is_end(x, y):
                return visit[info]
            for add_i, add_j in direction:
                ii, jj = x + add_i, y + add_j
                if in_range(ii, jj):
                    d = abs(heights[ii][jj] - heights[x][y])
                    tt = (ii, jj)
                    # if tt not in visit or visit[tt] > d:
                    #     pp = max(t, d)
                    #     queue.put((pp, (ii, jj)))
                    #     visit[(ii, jj)] = pp
                    
                    if tt not in visit:
                        pp = max(t, d)
                        queue.put((pp, (ii, jj)))
                        visit[(ii, jj)] = pp


func = Solution().minimumEffortPath
print(func([[1, 10, 6, 7, 9, 10, 4, 9]]))
print(func([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(func([]))
print(func([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(func([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
