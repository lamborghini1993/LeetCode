# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-25 11:23:23
"""
https://leetcode-cn.com/problems/regions-cut-by-slashes/
"""

from typing import List


class UnionFind(object):
    def __init__(self, n):
        self.father = list(range(n))
        self.n = n
        self.cnt = 1

    def find(self, x: int) -> int:
        father = self.father
        t = x
        while t != father[t]:
            t = father[t]
        while x != father[x]:
            x, father[x] = father[x], t
        return t

    def unite(self, x: int, y: int) -> bool:
        if x < 0 or y < 0:
            return
        xx, yy = self.find(x), self.find(y)
        if xx == yy:
            return
        if xx > yy:
            xx, yy = yy, xx
        self.father[xx] = yy
        self.cnt += 1
        return

    @property
    def num(self):
        cnt, info = 0, {}
        for i in range(self.n):
            t = self.find(i)
            if t not in info:
                info[t] = True
                cnt += 1
        return cnt


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid:
            return 0
        N, M = len(grid), len(grid[0])
        union = UnionFind(M * M * 4)
        for row, rows in enumerate(grid):
            for col, c in enumerate(rows):
                t = (row * M + col) * 4
                if c == "\\":
                    union.unite(t, t + 3)
                    union.unite(t + 1, t + 2)
                elif c == "/":
                    union.unite(t, t + 1)
                    union.unite(t + 2, t + 3)
                else:
                    union.unite(t, t + 1)
                    union.unite(t + 1, t + 2)
                    union.unite(t + 2, t + 3)
                    union.unite(t + 3, t)

                last_row = t + 3 - 4 * M
                last_col = t - 2
                if row:
                    union.unite(t + 1, last_row)
                if col:
                    union.unite(t, last_col)

        return union.num


func = Solution().regionsBySlashes
print(func([]))
print(func([" /", "/ "]))   # 2
print(func([" /", "  "]))   # 1
print(func(["\\/", "/\\"]))  # 4
print(func(["/\\", "\\/"]))    # 5
print(func(["//", "/ "]))    # 3
