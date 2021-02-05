# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-02-05 11:45:55
"""
https://leetcode-cn.com/problems/get-equal-substrings-within-budget/
"""


from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        lst = [abs(ord(c) - ord(t[i])) for i, c in enumerate(s)]
        i, j, cnt, result, N = 0, 0, 0, 0, len(s)
        while j < N:
            while j < N:
                cnt += lst[j]
                j += 1
                if cnt <= maxCost:
                    result = max(result, j - i)
                else:
                    break

            cnt -= lst[i]
            i += 1

        return result


func = Solution().equalSubstring
print(func("abcd", "qpab", 4))
print(func("abcd", "bcdf", 3))
print(func("abcd", "cdef", 3))
print(func("abcd", "acde", 0))
print(func("", "", 10))
