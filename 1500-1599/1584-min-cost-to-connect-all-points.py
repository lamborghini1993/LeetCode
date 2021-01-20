# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-19 17:02:33
"""
https://leetcode-cn.com/problems/min-cost-to-connect-all-points/
"""

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N, cos = len(points), []
        if N < 2:
            return 0
        for i, v in enumerate(points):
            for j in range(i + 1, N):
                x1, y1 = v
                x2, y2 = points[j]
                cos.append([(i, j), abs(x1 - x2) + abs(y1 - y2)])
        cos.sort(key=lambda x: x[1])
        result = 0

        parent = {x: x for x in range(N)}

        def find(x):
            t = x
            while parent[t] != t:
                t = parent[t]
            while parent[x] != t:
                x, parent[x] = parent[x], t
            return t

        for (x, y), v in cos:
            xx, yy = find(x), find(y)
            if xx != yy:
                parent[xx] = yy
                result += v
        return result

    def minCostConnectPoints_WA(self, points: List[List[int]]) -> int:
        N, cos = len(points), {}
        if N < 2:
            return 0
        for i, v in enumerate(points):
            for j in range(i + 1, N):
                x1, y1 = v
                x2, y2 = points[j]
                cos[(i, j)] = abs(x1 - x2) + abs(y1 - y2)

        result = 0
        vis = {}
        for i in range(N):
            if i in vis:
                continue
            min_j, min_v = i, 0
            for j in range(N):
                if j in vis or i == j:
                    continue
                value = cos[(i, j)] if i < j else cos[(j, i)]
                if not min_v or min_v > value:
                    min_j, min_v = j, value
            result += min_v
            vis[i] = True
            # vis[min_j] = True
        return result


func = Solution().minCostConnectPoints
print(func([[3, 12], [-2, 5], [-4, 1]]))
print(func([[0, 0], [1, 1], [1, 0], [-1, 1]]))
print(func([[-1000000, -1000000], [1000000, 1000000]]))
print(func([[0, 0]]))
