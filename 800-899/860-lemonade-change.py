# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-10 10:07:01
"""
https://leetcode-cn.com/problems/lemonade-change/
"""

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        moneyinfo = {}
        for bill in bills:
            moneyinfo[bill] = moneyinfo.get(bill, 0) + 1
            if bill == 5:
                continue
            bill -= 5
            while bill:
                if bill > 5 and moneyinfo.get(10, 0):
                    bill -= 10
                    moneyinfo[10] = moneyinfo[10] - 1
                elif moneyinfo.get(5, 0):
                    bill -= 5
                    moneyinfo[5] = moneyinfo[5] - 1
                else:
                    return False
        return True


func = Solution().lemonadeChange
print(func([5, 5, 5, 10, 20]))
