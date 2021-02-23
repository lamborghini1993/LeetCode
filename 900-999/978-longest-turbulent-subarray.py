# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-02-08 10:55:15
"""
https://leetcode-cn.com/problems/longest-turbulent-subarray/
"""

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        if N < 2:
            return N
        result, cnt, x = 1, 1, arr[0]
        up = None  # Flase-降 True-升 None-初始化

        for i in range(1, N):
            if up is None:
                if arr[i] > x:
                    up = True
                    cnt = 2
                elif arr[i] < x:
                    up = False
                    cnt = 2
                else:
                    cnt = 1

            elif up is True:
                if arr[i] > x:
                    up = True
                    cnt = 2
                elif arr[i] < x:
                    up = False
                    cnt += 1
                else:
                    up = None
                    cnt = 1

            elif up is False:
                if arr[i] > x:
                    up = True
                    cnt += 1
                elif arr[i] < x:
                    up = False
                    cnt = 2
                else:
                    up = None
                    cnt = 1

            result = max(result, cnt)
            x = arr[i]

        return result


func = Solution().maxTurbulenceSize
print(func([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(func([4, 8, 12, 16]))
print(func([100]))
print(func([2, 3]))
print(func([3, 3]))
print(func([]))
print(func([1, 2, 1, 3, 3, 1, 2, 1, 5]))
