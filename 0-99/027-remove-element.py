# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-11 11:40:40
"""
https://leetcode-cn.com/problems/remove-element/
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast_v in nums:
            if fast_v != val:
                nums[slow] = fast_v
                slow += 1
        return slow

    # 双指针-难理解
    def removeElement_2(self, nums: List[int], val: int) -> int:
        i, cnt, n = 0, 0, len(nums) - 1
        while i <= n:
            if nums[i] != val:
                i += 1
                cnt += 1
                continue
            while n >= i:
                if nums[n] != val:
                    break
                n -= 1
            if n < i:
                break
            nums[i], nums[n] = nums[n], nums[i]
            cnt += 1
            n -= 1
            i += 1
        return nums, cnt


func = Solution().removeElement
print(func([4, 5], 5))
print(func([3, 3, 3], 3))
print(func([3, 2, 2, 3], 3))
print(func([0, 1, 2, 2, 3, 0, 4, 2], 2))
