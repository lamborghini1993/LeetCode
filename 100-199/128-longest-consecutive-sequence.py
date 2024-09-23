# -*- coding:utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2020-06-06 21:05:27
@Description: https://leetcode-cn.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has_dict = {}
        max_lenght = 0
        for x in nums:
            if x not in has_dict:
                left_num = has_dict.get(x - 1, 0)
                right_num = has_dict.get(x + 1, 0)
                cur_lenght = left_num + 1 + right_num
                max_lenght = max(max_lenght, cur_lenght)

                has_dict[x] = cur_lenght
                has_dict[x - left_num] = cur_lenght
                has_dict[x + right_num] = cur_lenght

        return max_lenght

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     nums = set(nums)
    #     result = 0
    #     for x in nums:
    #         if x - 1 not in nums:
    #             temp = 1
    #             while x + 1 in nums:
    #                 temp += 1
    #                 x += 1
    #             result = max(result, temp)
    #     return result


func = Solution().longestConsecutive
print(func([100, 4, 200, 1, 3, 2]))
print(func([]))
print(func([3]))
