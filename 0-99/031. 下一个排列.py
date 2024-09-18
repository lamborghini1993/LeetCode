from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从后往前找，找到第一个降序的 i
        # 从后往前找，找到第一个比它大的 j，交换i-j
        # 翻转j + 1 后面
        n = len(nums)

        # 从后往前找，找到第一个降序的 i
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # 从后往前找，找到第一个比它大的 j，交换i-j
        if i > 0:
            j = n - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # 翻转j + 1 后面
        nums[i:] = sorted(nums[i:])
        print(nums)


obj = Solution()
print(obj.nextPermutation([4, 2, 5, 5, 3, 2]))
print(obj.nextPermutation([4, 2, 0, 2, 3, 2, 0]))
print(obj.nextPermutation([1, 2, 3]))
print(obj.nextPermutation([3, 2, 1]))
print(obj.nextPermutation([1, 1, 5]))
print(obj.nextPermutation([1, 3, 2]))
print(obj.nextPermutation([1]))


4224432

4232244
