from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visit = {start: True}
        q = deque()
        q.append(start)
        while len(q) > 0:
            x = q.popleft()
            if arr[x] == 0:
                return True

            for v in (-1, 1):
                t = x + v * arr[x]
                if 0 <= t < n and t not in visit:

                    visit[t] = True
                    q.append(t)
        return False


func = Solution().canReach
print(func([4, 2, 3, 0, 3, 1, 2], 5))
print(func([4, 2, 3, 0, 3, 1, 2], 0))
print(func([3, 0, 2, 1, 2], 2))
print(func([0], 0))
