# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-21 21:27:51
"""
https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
"""

from typing import List


class UnionFind(object):
    def __init__(self, n):
        self.father = list(range(n))
        self.n = n
        self.v = 0
        self.cnt = 1

    def find(self, x: int) -> int:
        father = self.father
        t = x
        while t != father[t]:
            t = father[t]
        while x != father[x]:
            x, father[x] = father[x], t
        return t

    def unite(self, x: int, y: int, v: int) -> bool:
        xx, yy = self.find(x), self.find(y)
        if xx == yy:
            return False
        if xx > yy:
            xx, yy = yy, xx
        self.father[xx] = yy
        self.v += v
        self.cnt += 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        1. 求出最小生成树的权值和
        2. 
            1. 如果最小生成树中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。
            2. 最先考虑这条边，设最终得到的最小生成树权值相等，极为非关键边。
        """
        for i, lst in enumerate(edges):
            lst.append(i)
        edges.sort(key=lambda x: x[2])

        oUnit = UnionFind(n)
        for tt in edges:
            x, y, v, _ = tt
            oUnit.unite(x, y, v)

        resutl1, result2 = [], []
        for tt in edges:
            x, y, v, i = tt

            # 判断是否为关键边:如果最小生成树中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。
            tUnit = UnionFind(n)
            # tUnit.unite(x, y, v)
            for zz in edges:
                xx, yy, vv, ii = zz
                if ii == i:
                    continue
                tUnit.unite(xx, yy, vv)

            if tUnit.cnt != n or tUnit.v != oUnit.v:
                resutl1.append(i)
                continue

            # 判断是否为伪关键边:可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
            # 也就是说，我们可以在计算最小生成树的过程中，最先考虑这条边，即最先将这条边的两个端点在并查集中合并。
            # 设最终得到的最小生成树权值为 vv，如果 v = \textit{value}v=value，那么这条边就是伪关键边
            pUnit = UnionFind(n)
            pUnit.unite(x, y, v)
            for zz in edges:
                xx, yy, vv, ii = zz
                if ii == i:
                    continue
                pUnit.unite(xx, yy, vv)

            if pUnit.cnt == n and pUnit.v == oUnit.v:
                result2.append(i)
                continue

        return resutl1, result2

    def findCriticalAndPseudoCriticalEdges_WA(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        权值从小到大排序，如果某个权值有加入发现是连通的，说明是非关键路径，否则是关键路径
        WA: 6, [[0, 1, 2], [0, 2, 5], [2, 3, 5], [1, 4, 4], [2, 5, 5], [4, 5, 2]]
        """
        for i, lst in enumerate(edges):
            lst.append(i)
        edges.sort(key=lambda x: x[2])
        father = {x: x for x in range(n)}

        def find(x):
            t = x
            while t != father[t]:
                t = father[t]
            while x != father[x]:
                x, father[x] = father[x], t
            return t

        resutl1, result2 = [], []

        def add(is_key, lst):
            if is_key:
                resutl1.extend(lst)
            else:
                if len(lst) >= 2:
                    result2.extend(lst)

        last_v, v_lst, is_key = -1, [], True
        for tt in edges:
            x, y, v, index = tt
            xx, yy = find(x), find(y)

            if v != last_v:
                add(is_key, v_lst)
                last_v, v_lst, is_key = v, [], True

            if xx != yy:
                father[xx] = yy
                v_lst.append(index)
            else:
                is_key = False
                v_lst.append(index)

        add(is_key, v_lst)

        return resutl1, result2


func = Solution().findCriticalAndPseudoCriticalEdges
print(func(4, [[3, 1, 1], [1, 2, 5], [2, 3, 5], [2, 0, 5]]))
print(func(6, [[0, 1, 2], [0, 2, 5], [2, 3, 5], [1, 4, 4], [2, 5, 5], [4, 5, 2]]))
print(func(5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]))
print(func(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]))
