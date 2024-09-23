from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = 0
        curPos = 0
        while curPos < n:
            step += 1
            maxPos, maxT = 0, 0
            for i in range(nums[curPos]):
                t = curPos + i + 1
                if t >= n - 1:
                    return step
                if t + nums[t] >= maxPos:
                    maxPos, maxT = t + nums[t], t
            curPos = maxT

        return step

    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     step = 0
    #     maxPos = 0
    #     end = 0
    #     for i in range(n):
    #         if maxPos >= i:
    #             maxPos = max(maxPos, i + nums[i])
    #             if i == end:
    #                 end = maxPos
    #                 step += 1

    #     return step

    # def jump(self, nums: List[int]) -> int:
    #     """954ms"""
    #     n = len(nums)
    #     pos = n - 1
    #     step = 0
    #     while pos > 0:
    #         for i in range(pos):
    #             if i + nums[i] >= pos:
    #                 step += 1
    #                 pos = i
    #                 break
    #     return step


func = Solution().jump
print(func([2, 3, 1, 1, 4]))
print(func([2, 3, 0, 1, 4]))
