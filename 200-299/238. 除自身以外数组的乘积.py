from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(0, n):
            if i:
                left[i] = nums[i] * left[i - 1]
            else:
                left[i] = nums[i]

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                right[i] = nums[i]
            else:
                right[i] = nums[i] * right[i + 1]

        result = []
        for i in range(n):
            ll = left[i - 1] if i - 1 >= 0 else 1
            rr = right[i + 1] if i + 1 < n else 1
            result.append(ll * rr)
        return result


func = Solution().productExceptSelf
print(func([1, 2, 3, 4]))
print(func([-1, 1, 0, -3, 3]))
