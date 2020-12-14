# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-10 10:02:24
"""
https://leetcode-cn.com/problems/unique-paths/
C(m+n-2, min(m-1, n-1))
"""

import math
import sys


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 2 or n < 2:
            return 1
        t = m + n - 2
        p = min(m - 1, n - 1)
        v = 1
        for i in range(p):
            v = v * (t - i) // (i + 1)

        return v
