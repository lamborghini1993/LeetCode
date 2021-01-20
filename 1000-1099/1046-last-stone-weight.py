# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-30 15:56:03
"""
https://leetcode-cn.com/problems/last-stone-weight/
"""

from queue import PriorityQueue
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = PriorityQueue()
        for stone in stones:
            queue.put((-stone, stone))
        while queue.qsize() > 1:
            a, b = queue.get(), queue.get()
            t = abs(a[1] - b[1])
            queue.put((-t, t))
        return queue.get()[1]


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
