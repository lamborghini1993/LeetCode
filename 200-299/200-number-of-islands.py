# -*- coding:utf-8 -*-
# Author: lamborghini1993
"""
https://leetcode.cn/problems/number-of-islands/description
"""

from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        result = 0

        def bfs(a, b):
            grid[a][b] = "x"
            stack = [(a, b)]
            while stack:
                x, y = stack.pop()
                for addx, addy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    newa, newb = x + addx, y + addy
                    if 0 <= newa < n and 0 <= newb < m and grid[newa][newb] == "1":
                        stack.append((newa, newb))
                        grid[newa][newb] = "x"

        for i, lst in enumerate(grid):
            for j, v in enumerate(lst):
                if v == "1":
                    result += 1
                    bfs(i, j)

        return result
    
    def numIslands_1(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        result = 0

        def dfs(a, b):
            grid[a][b] = "x"
            for addx, addy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                newa, newb = a + addx, b + addy
                if 0 <= newa < n and 0 <= newb < m and grid[newa][newb] == "1":
                    dfs(newa, newb)

        for i, lst in enumerate(grid):
            for j, v in enumerate(lst):
                if v == "1":
                    result += 1
                    dfs(i, j)

        return result