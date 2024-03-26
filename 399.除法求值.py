#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 并查集问题
        parent = {}

        for i, v in enumerate(values):
            a, b = equations[i]
            parent[a] = (b, 2)

        result = []


        for a, b in equations:
            parent[a] = (a, 1)
            parent[b] = (b, 1)
        
        def union(x, y, v):
            pass

        for i, v in enumerate(values):
            a, b = equations[i]
            union(a, b, v)


# @lc code=end

