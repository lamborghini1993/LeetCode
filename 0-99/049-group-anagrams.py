# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-14 19:35:57
"""
https://leetcode-cn.com/problems/group-anagrams/
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        info = {}
        for i, string in enumerate(strs):
            new_str = "".join(sorted(string))
            data = info.setdefault(new_str, [])
            data.append(i)
        result = []
        for _, lst in info.items():
            tt = []
            for i in lst:
                tt.append(strs[i])
            result.append(tt)
        return result

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     info = {}
    #     for string in strs:
    #         v = 0
    #         for c in string:
    #             v += 1 << (ord(c) - 97)
    #         data = info.setdefault(len(string), {}).setdefault(v, [])
    #         data.append(string)
    #     result = []
    #     for _, data1 in info.items():
    #         for __, lst in data1.items():
    #             result.append(lst)
    #     return result


func = Solution().groupAnagrams
print(func(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(func(["ron", "huh", "gay", "tow", "moe", "tie", "who", "ion", "rep", "bob", "gte", "lee", "jay", "may", "wyo", "bay", "woe", "lip", "tit",
            "apt", "doe", "hot", "dis", "fop", "low", "bop", "apt", "dun", "ben", "paw", "ere", "bad", "ill", "fla", "mop", "tut", "sol", "peg", "pop", "les"]))
