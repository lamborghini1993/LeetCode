# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-21 17:34:38
@UpdateDate: 2020-05-21 17:42:27
'''

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] > amount else dp[amount]
