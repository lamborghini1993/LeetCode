from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        h = 0
        while h < n and citations[-h - 1] > h:
            h += 1

        return h


obj = Solution()
print(obj.hIndex([3, 0, 6, 1, 5]))
print(obj.hIndex([1, 3, 1]))
print(obj.hIndex([1]))
