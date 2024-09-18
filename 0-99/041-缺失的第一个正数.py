from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        for i in range(N):
            while nums[i] > 0 and nums[i] <= N and nums[i] != nums[nums[i] - 1]:
                swap(i, nums[i] - 1)

        for i, x in enumerate(nums):
            if x != i + 1:
                return i + 1

        return N + 1


obj = Solution()
print(obj.firstMissingPositive([1, 2, 0]))
print(obj.firstMissingPositive([3, 4, -1, 1]))
print(obj.firstMissingPositive([7, 8, 9, 11, 12]))
