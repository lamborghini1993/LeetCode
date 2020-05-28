class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            value = target - v
            if value not in nums:
                continue
            j = nums.index(value)
            if i != j:
                return [i, j]
        return None
