# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-11-17 16:10:01
"""
https://leetcode-cn.com/problems/matrix-cells-in-distance-order/
"""

from queue import Queue
from typing import List

DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Solution:

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        visit = {}
        result = []
        queue = Queue()

        def add(x: int, y: int):
            visit[(x, y)] = True
            queue.put((x, y))
            result.append([x, y])

        def in_bounds(x: int, y: int) -> bool:
            if x < 0 or x >= R:
                return False
            if y < 0 or y >= C:
                return False
            return True

        add(r0, c0)
        while not queue.empty():
            pos = queue.get()
            for tmp in DIR:
                tx = pos[0] + tmp[0]
                ty = pos[1] + tmp[1]
                if not in_bounds(tx, ty) or (tx, ty) in visit:
                    continue
                add(tx, ty)

        return result


func = Solution().allCellsDistOrder
print(func(1, 2, 0, 0))
print(func(2, 2, 0, 1))
print(func(2, 3, 1, 2))
