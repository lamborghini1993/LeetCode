# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-06 21:05:27
@Description: https://leetcode-cn.com/problems/longest-consecutive-sequence/
'''

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        for x in nums:
            if x - 1 not in nums:
                temp = 1
                while x + 1 in nums:
                    temp += 1
                    x += 1
                result = max(result, temp)
        return result


func = Solution().longestConsecutive
print(func([]))
print(func([3]))
print(func([100, 4, 200, 1, 3, 2]))
