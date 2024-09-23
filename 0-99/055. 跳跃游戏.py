from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        end = 0
        maxPos = 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
        return maxPos >= n - 1


func = Solution().canJump
print(func([2, 3, 1, 1, 4]))
print(func([3, 2, 1, 0, 4]))
