# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-19 18:40:28
@UpdateDate: 2020-05-19 18:50:48
'''

from typing import List
class Solution:
    N = 1337
    def _pow(self, a: int, b: int):
        result = 1
        for _ in range(b):
            result = (result * a) % self.N
        return result
            
    def superPow(self, a: int, b: List[int]) -> int:
        a = a % self.N
        if len(b) == 1:
            return self._pow(a, b[0])
        end = b.pop()
        a1 = self._pow(a, end)
        b1 = self._pow(self.superPow(a, b), 10)
        return (a1 * b1) % self.N

obj = Solution()
a = 2
b = [1, 0]
print(obj.superPow(a, b))
