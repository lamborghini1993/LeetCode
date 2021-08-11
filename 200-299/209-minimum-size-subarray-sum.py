# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-11 16:11:07
"""
https://leetcode-cn.com/problems/minimum-size-subarray-sum/
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        i = total = 0
        ans = len(nums)
        for j, value in enumerate(nums):
            total += value
            while total >= target:
                ans = min(ans, j - i + 1)
                total -= nums[i]
                i += 1
        return ans

    def minSubArrayLen_2(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        i = j = total = 0
        ans = len(nums)
        while j < len(nums):
            if nums[j] >= target:
                return 1
            total += nums[j]
            if total < target:
                j += 1
                continue
            ans = min(ans, j - i + 1)
            while i < j and total - nums[i] >= target:
                total -= nums[i]
                i += 1
                ans = min(ans, j - i + 1)
            j += 1
        return ans


func = Solution().minSubArrayLen
print(func(7, [2, 3, 1, 2, 4, 3]))
print(func(7, [2, 3, 11, 2, 4, 3]))
print(func(17, [1, 1, 1, 1, 1, 1, 1, 1]))
