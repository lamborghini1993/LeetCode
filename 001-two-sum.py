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


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dInfo = {}
        for x, xValue in enumerate(nums):
            yValue = target - xValue
            if yValue in dInfo:
                return [dInfo[yValue], x]
            dInfo[xValue] = x
        return None

print(Solution2().twoSum([2,7,11,15], 9))