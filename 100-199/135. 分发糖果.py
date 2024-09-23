from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        left = [1] * N  # 从左到右满足
        right = [1] * N

        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for j in range(N - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                right[j] = right[j + 1] + 1

        total = 0
        for k in range(N):
            total += max(left[k], right[k])
        return total


func = Solution().candy
print(func([1, 0, 2]))
print(func([1, 2, 2]))
