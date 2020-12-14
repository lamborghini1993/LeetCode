# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-04 16:34:36
"""

"""

from typing import List
from collections import Counter


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        data = Counter(nums)
        while data:
            # 贪心思想：找到当前最小的数
            first_num = cur_num = min(data.items(), key=lambda v: v[0])[0]
            while True:
                next_num = cur_num + 1

                # 当前数-1
                if data[cur_num] == 1:
                    del data[cur_num]
                else:
                    data[cur_num] -= 1

                # 如果下一个数不在data or 当前的数剩下的数量 >= 下一个数的数量
                if next_num not in data or data.get(cur_num, 0) >= data[next_num]:
                    break
                cur_num = next_num
            
            # 当找到末尾时判断长度
            if cur_num - first_num < 2:
                return False

        return True # 当data为空时说明可以


func = Solution().isPossible
print(func([1, 2, 3, 3, 4, 5]))
print(func([1, 2, 3, 3, 4, 6]))
print(func([2, 3, 3, 4, 4, 5]))
print(func([1, 2, 2, 3, 3, 4, 4, 5]))
print(func([1, 2, 2, 3, 3, 3, 4, 4, 5]))
print(func([1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]))
