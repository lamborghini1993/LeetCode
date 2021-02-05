# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-02-04 10:58:57
"""
https://leetcode-cn.com/problems/maximum-average-subarray-i/
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = tmp = sum(nums[:k])
        for i in range(k, len(nums)):
            tmp += nums[i] - nums[i - k]
            result = max(result, tmp)
        return result / k
