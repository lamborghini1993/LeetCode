#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_greed = [0] * numCourses
        edge = defaultdict(list)
        for a, b in prerequisites:
            in_greed[b] += 1
            edge[a].append(b)

        stack = []
        for i, v in enumerate(in_greed):
            if not v:
                stack.append(i)

        while stack:
            s = stack.pop()
            for x in edge[s]:
                in_greed[x] -= 1
                if in_greed[x] == 0:
                    stack.append(x)

        return sum(in_greed) == 0

# @lc code=end

print(Solution().canFinish(2, [[1,0],[0,1]]))
print(Solution().canFinish(3, [[1,0],[0,2], [2, 1]]))

print(Solution().canFinish(2, [[1,0]]))
print(Solution().canFinish(3, [[1,0],[1,2]]))
print(Solution().canFinish(3, [[1,0],[1,2], [2, 0]]))
print(Solution().canFinish(3, [[1,0],[2,1]]))
