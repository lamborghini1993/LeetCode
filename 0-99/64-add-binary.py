# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-23 17:31:16
@Description: https://leetcode-cn.com/problems/add-binary/
'''


class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    def addBinary(self, a: str, b: str) -> str:
        """模拟二进制加法"""
        tmp, ans = 0, []
        n = max(len(a), len(b))
        for i in range(0, n):
            x = int(a[len(a)-i-1]) if i < len(a) else 0
            y = int(b[len(b)-i-1]) if i < len(b) else 0
            tmp += x + y
            ans.append(str(tmp % 2))
            tmp = tmp >> 1
        if tmp:
            ans.append(str(tmp))
        ans.reverse()
        return "".join(ans)


func = Solution().addBinary
print(func("11", "1"))
print(func("1010", "1011"))
