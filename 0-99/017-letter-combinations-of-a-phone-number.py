# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-15 23:00:24
"""
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        info = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        ans = []
        def dfs(s, n):
            if n == len(digits):
                ans.append(s)
                return
            for t in info[digits[n]]:
                dfs(s + t, n+1)

        dfs("", 0)
        return ans

func = Solution().letterCombinations
print(func("23"))
print(func("2"))
print(func(""))
