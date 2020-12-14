# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-03 19:43:34
"""

"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        cnt, lst = 0, [0] * n
        for i in range(2, n):
            if lst[i]:
                continue
            cnt += 1
            for j in range(i, n, i):
                lst[j] = 1
        return cnt


func = Solution().countPrimes
print(func(0))
print(func(1))
print(func(2))
print(func(10))
print(func(123456))
