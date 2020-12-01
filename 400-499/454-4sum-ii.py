# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-11-30 20:06:06
"""
https://leetcode-cn.com/problems/4sum-ii/
"""

from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        N, value1, value2 = len(A), {}, {}
        for i in range(N):
            for j in range(N):
                v1, v2 = A[i] + B[j], C[i] + D[j]
                value1[v1] = value1.get(v1, 0) + 1
                value2[v2] = value2.get(v2, 0) + 1
        result = 0
        for v1, n1 in value1.items():
            n2 = value2.get(-v1, 0)
            if n2:
                result += n1 * n2
        return result


func = Solution().fourSumCount
print(func([1, 2], [-2, -1], [-1, 2], [0, 2]))
