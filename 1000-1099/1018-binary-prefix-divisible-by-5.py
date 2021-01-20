# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-01-14 15:59:32
"""
https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/
"""

from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        cnt, result = 0, []
        for i in A:
            cnt = cnt * 2 + i
            result.append(not cnt % 5)
        return result


func = Solution().prefixesDivBy5
print(func([0, 1, 1]))
print(func([1, 1, 1]))
print(func([0, 1, 1, 1, 1, 1]))
print(func([1, 1, 1, 0, 1]))
