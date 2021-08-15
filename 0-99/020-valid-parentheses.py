# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-15 23:10:17
"""
https://leetcode-cn.com/problems/valid-parentheses/
"""

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for c in s:
            if c in "([{":
                q.append(c)
            else:
                if not q:
                    return False
                t = q.pop()
                if c == ")":
                    if t != "(":
                        return False
                elif c == "}":
                    if t != "{":
                        return False
                elif c == "]":
                    if t != "[":
                        return False

        if q:
            return False
        return True

func = Solution().isValid
print(func("()"))
print(func("()[]{}"))
print(func("(]"))
print(func("([)]"))
print(func("{[]}"))
print(func(""))
print(func("["))
