# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-15 20:14:20
@Description: https://leetcode-cn.com/problems/longest-common-prefix/
'''


from typing import List


class Solution:
    def same(self, index, strs):
        if len(strs[0]) <= index:
            return False
        c = strs[0][index]
        for string in strs:
            if len(string) <= index or string[index] != c:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        index = 0
        while True:
            if self.same(index, strs):
                index += 1
            else:
                return strs[0][:index]
        return ""


func = Solution().longestCommonPrefix
print(func(["flower", "flow", "flight"]))
print(func(["flower", "flow", ""]))
print(func([]))
print(func(["dog", "racecar", "car"]))
