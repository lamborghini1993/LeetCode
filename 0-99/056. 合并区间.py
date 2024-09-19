from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        lastx, lasty = None, None
        for i, inter in enumerate(intervals):
            x, y = inter
            if lastx is None:
                lastx, lasty = x, y
                continue

            if lasty >= x:
                lasty = max(lasty, y)
            else:
                result.append([lastx, lasty])
                lastx, lasty = x, y

        result.append([lastx, lasty])
        return result


obj = Solution()
print(obj.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(obj.merge([[8, 10], [15, 18], [1, 3], [2, 6]]))
print(obj.merge([[1, 4], [4, 5]]))
print(obj.merge([[1, 4]]))
