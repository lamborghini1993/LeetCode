from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []

        def find_replace_min_x(t):
            if not ans:
                ans.append(t)
                return
            # ans从小到大排序，找到ans中第一个大于t的位置
            l, r = 0, len(ans)
            while l < r:
                m = (l + r) // 2
                if ans[m] < t:
                    l = m + 1
                else:
                    r = m
            if l < len(ans):
                ans[l] = t
            else:
                ans.append(t)

        for x in nums:
            find_replace_min_x(x)

        return len(ans)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     # dp[i] 表示以 i 结尾的最长递增子序列
    #     dp = [1] * n
    #     result = 1
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #         result = max(result, dp[i])
    #     return result


obj = Solution()
print(obj.lengthOfLIS([4, 10, 1, 2, 3, 9]))
print(obj.lengthOfLIS([4, 10, 4, 3, 8, 9]))
print(obj.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(obj.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(obj.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
