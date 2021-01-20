# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-05 17:12:18
"""
https://leetcode-cn.com/problems/positions-of-large-groups/
"""

from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        tc, cnt, result = "", 0, []
        for i, c in enumerate(s):
            if c == tc:
                cnt += 1
                continue
            if cnt > 2:
                result.append([i - cnt, i - 1])
            tc, cnt = c, 1
        if cnt > 2:
            result.append([i - cnt + 1, i])
        return result


func = Solution().largeGroupPositions
print(func("aaa"))
print(func("abbxxxxzzy"))
print(func("abc"))
print(func(""))
print(func("abcdddeeeeaabbbcd"))
print(func("aba"))
