# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-17 21:00:54
@Description: https://leetcode-cn.com/problems/best-sightseeing-pair/
'''

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans, mx = 0, A[0]
        for j in range(1, len(A)):
            ans = max(ans, mx + A[j]-j)
            mx = max(mx, A[j]+j)
        return ans
