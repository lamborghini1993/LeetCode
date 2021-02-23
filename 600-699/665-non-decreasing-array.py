# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-02-07 11:26:45
"""
https://leetcode-cn.com/problems/non-decreasing-array/
"""

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if cnt > 1:
                    return False
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True


func = Solution().checkPossibility
print(func([4, 2, 3]))
print(func([3, 4, 2, 3]))
print(func([3, 4, 2]))
print(func([4, 2, 1]))
