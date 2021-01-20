# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-07 14:20:03
"""
https://leetcode-cn.com/problems/number-of-provinces/
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """dfs"""
        if not isConnected:
            return 0
        n = len(isConnected)
        maps, visit = {}, {}
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    maps.setdefault(i, []).append(j)
                    maps.setdefault(j, []).append(i)

        def dfs(t):
            if t in maps and visit.get(t, 0) != 1:
                visit[t] = 1
                for p in maps[t]:
                    dfs(p)
            visit[t] = 1

        cnt = 0
        for i in range(n):
            if visit.get(i, 0) != 1:  # 1 访问过
                cnt += 1
                dfs(i)

        return cnt

    def findCircleNum_AC(self, isConnected: List[List[int]]) -> int:
        """并查集思想"""
        if not isConnected:
            return 0
        n = len(isConnected)
        father = {x: x for x in range(n)}

        def find(t):
            r = t
            while father[t] != t:
                t = father[t]
            while r != t:
                r, father[r] = father[r], t
            return t

        def update(x, y):
            xx, yy = find(x), find(y)
            if xx != yy:
                father[xx] = yy

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    update(i, j)

        cnt = 0
        for i in range(n):
            if i == find(i):
                cnt += 1
        return cnt


func = Solution().findCircleNum
print(func([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
print(func([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]))
print(func([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
