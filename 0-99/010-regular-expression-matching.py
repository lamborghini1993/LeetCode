# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-05-29 19:37:45
@Description: 
https://leetcode-cn.com/problems/regular-expression-matching/
https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-zhi-zheng-ze-biao-da
见 love2\19-zheng-ze-biao-da-shi-pi-pei-lcof.py
'''


class Solution:
    """带备忘录递归匹配字符串是否相等"""

    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()  # 备忘录

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            first_match = i < len(s) and p[j] in (s[i], ".")
            if j + 2 <= len(p) and p[j+1] == "*":
                ans = dp(i, j+2) or (first_match and dp(i+1, j))
            else:
                ans = first_match and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)


func = Solution().isMatch
print(func("123", "1.3*3"))
print(func("ab", ".*3"))
