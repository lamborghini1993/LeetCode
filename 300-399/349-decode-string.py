# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-28 16:20:47
@UpdateDate: 2020-05-28 16:48:09
https://leetcode-cn.com/problems/decode-string/
'''


class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c.isdigit():
                multi = multi * 10 + int(c)
            elif c == "[":
                stack.append([res, multi])
                res, multi = "", 0
            elif c == "]":
                last_res, cur_multi = stack.pop()
                res = last_res + cur_multi * res
            else:
                res += c
        return res


func = Solution().decodeString
print(func("3[a]2[bc]"))
print(func("3[a2[c]]"))
print(func("2[abc]3[cd]ef"))
