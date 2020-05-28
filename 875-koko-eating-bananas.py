# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-20 18:55:12
@UpdateDate: 2020-05-20 19:08:07
'''

from typing import List

class Solution:
    def _get_hour(self, piles, speed):
        _hour = 0
        for pile in piles:
            t = 1 if pile % speed else 0
            _hour += pile // speed + t
        return _hour
        
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        minSpeed, maxSpeed = 1, 10**9
        while minSpeed < maxSpeed:
            mid = (minSpeed + maxSpeed) // 2
            hour = self._get_hour(piles, mid)
            if hour > H:
                minSpeed = mid + 1
            else:
                maxSpeed = mid
        return (minSpeed + maxSpeed) // 2
        
onj = Solution()
piles = [30, 11, 23, 4, 20]
print(onj.minEatingSpeed(piles, 6))
