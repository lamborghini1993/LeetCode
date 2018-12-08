class Solution:
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
