# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-05-29 17:02:28
@Description: 
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-zhi-zheng-ze-biao-da
'''

# ? 递归匹配字符串是否相等
# class Solution:
#     def __init__(self):
#         self.match = True

#     def isMatch(self, s: str, p: str) -> bool:
#         if not self.match: return
#         if not (s or p): return
#         if s and p:
#             if s[0] == p[0]:
#                 self.isMatch(s[1:], p[1:])
#             return
#         self.match = False

#     def debug(self, s, p):
#         self.match = True
#         self.isMatch(s, p)
#         return self.match

# func = Solution().debug
# print(func("123", "123"))


# ? 递归匹配字符串是否相等-包含(.)
# class Solution:
#     def __init__(self):
#         self.match = True

#     def isMatch(self, s: str, p: str) -> bool:
#         if not self.match: return
#         if not (s or p): return
#         if s and p:
#             if p[0] in (s[0], "."):
#                 self.isMatch(s[1:], p[1:])
#             return
#         self.match = False

#     def debug(self, s, p):
#         self.match = True
#         self.isMatch(s, p)
#         return self.match

# func = Solution().debug
# print(func("123", "1.33"))


# # ? 递归匹配字符串是否相等-包含(.*)
# def isMatch(text, pattern) -> bool:
#     if not pattern:
#         return not text
#     first_match = text and pattern[0] in {text[0], '.'}
#     if len(pattern) >= 2 and pattern[1] == '*':
#         return isMatch(text, pattern[2:]) or first_match and isMatch(text[1:], pattern)
#     else:
#         return first_match and isMatch(text[1:], pattern[1:])


# class Solution:
#     """递归匹配字符串是否相等"""

#     def isMatch(self, s: str, p: str) -> bool:
#         if not p:
#             return not s
#         first_match = len(s) > 0 and p[0] in (s[0], ".")
#         if len(p) >= 2 and p[1] == "*":
#             return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
#         return first_match and self.isMatch(s[1:], p[1:])


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
            print(f"{i} {j} : {ans}")
            return ans
        return dp(0, 0)


func = Solution().isMatch
print(func("123", "1.3*3"))
print(func("ab", ".*3"))
