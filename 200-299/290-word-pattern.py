# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-16 18:51:21
"""
https://leetcode-cn.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split(" ")
        if len(pattern) != len(lst):
            return False
        map_info = {}
        reversed_map = {}
        for i, c in enumerate(pattern):
            s1 = map_info.get(c)
            s2 = lst[i]
            if s1:
                if s1 != s2:
                    return False
            else:
                if s2 in reversed_map:
                    return False
                map_info[c] = s2
                reversed_map[s2] = c
        return True

func = Solution().wordPattern
print(func("abba", "dog cat cat dog"))
print(func("abba", "dog cat cat fish"))
print(func("aaaa", "dog cat cat dog"))
print(func("abba", "dog dog dog dog"))
