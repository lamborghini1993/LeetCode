# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-11-30 17:37:41
"""
https://leetcode-cn.com/problems/reorganize-string/
"""

from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return ""
        info = Counter(S)
        # 找出出现最多次数的字母和次数
        max_c, max_num = max(info.items(), key=lambda x: x[1])
        if max_num > (len(S) + 1) // 2:
            return ""

        result = [""] * len(S)
        # 先放出现最多次数的字母
        for i in range(max_num):
            result[i * 2] = max_c

        index = max_num * 2
        if index >= len(S):
            index = 1
        del info[max_c]
        for c, v in info.items():
            while v:
                result[index] = c
                index += 2
                if index >= len(S):
                    index = 1
                v -= 1
        return "".join(result)


func = Solution().reorganizeString
print(func("baaba"))
print(func("aab"))
print(func("ABCJASAFAAFA"))
