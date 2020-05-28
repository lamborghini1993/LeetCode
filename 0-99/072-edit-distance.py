# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-19 19:13:58
@UpdateDate: 2020-05-19 19:23:35
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for __ in range(l2 + 1)]for _ in range(l1 + 1)]
        for x in range(l1 + 1):
            dp[x][0] = x
        for y in range(l2 + 1):
            dp[0][y] = y
        for x in range(1, l1 + 1):
            for y in range(1, l2 + 1):
                if word1[x - 1] == word2[y - 1]:
                    dp[x][y] = dp[x - 1][y - 1]
                else:
                    dp[x][y] = min(
                        dp[x - 1][y - 1],
                        dp[x - 1][y],
                        dp[x][y - 1]
                    ) + 1

        return dp[l1][l2]


obj = Solution()
print(obj.minDistance("", "a"))
