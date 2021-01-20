# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-31 16:18:06
"""
https://leetcode-cn.com/problems/non-overlapping-intervals/
"""

from typing import List


class Solution:
    def is_cross(self, a, b):
        if a[0] >= b[1]:
            return False
        if a[1] <= b[0]:
            return False
        return True

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """贪心思想
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        N = len(intervals)
        right, cnt = intervals[0][1], 1
        for i in range(1, N):
            if intervals[i][0] >= right:
                cnt += 1
                right = intervals[i][1]
        return N - cnt

    def eraseOverlapIntervals_ac(self, intervals: List[List[int]]) -> int:
        """动态规划思想
        找出重叠的最大数量
        """
        if not intervals:
            return 0
        intervals.sort()
        N = len(intervals)
        dp = [-1] * N
        dp[0] = 1
        for i in range(1, N):
            dp[i] = max([dp[j] for j in range(0, i) if not self.is_cross(intervals[i], intervals[j])], default=0) + 1
        return N - max(dp)

    def eraseOverlapIntervals_wa(self, intervals: List[List[int]]) -> int:
        """
        [[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]        5 != 4
        """
        info = {}
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if not self.is_cross(intervals[i], intervals[j]):
                    continue
                info.setdefault(i, []).append(j)
                info.setdefault(j, []).append(i)
        result = 0
        while info:
            max_index, max_num = -1, -1
            for i, lst in info.items():
                if len(lst) > max_num:
                    max_index, max_num = i, len(lst)
            for v in info[max_index]:
                info[v].remove(max_index)
                if not info[v]:
                    del info[v]
            del info[max_index]
            result += 1
        return result


func = Solution().eraseOverlapIntervals
print(func([]))
print(func([[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]))  # 5 != 4
print(func([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(func([[1, 2], [1, 2], [1, 2]]))
print(func([[1, 2], [2, 3]]))
