#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List
import copy
# @lc code=start
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        # dfs
        result = []
        path = []

        def dfs(t):
            if len(path) == k:
                result.append(copy.copy(path))
                return
            for x in range(t + 1, n + 1):
                path.append(x)
                dfs(x)
                path.pop()

        
        for i in range(1, n + 1):
            path.append(i)
            dfs(i)
            path.pop()
        
        return result

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        # dfs
        result = []

        def dfs(t, tmp_lst):
            tmp_lst.append(t)
            if len(tmp_lst) == k:
                result.append(tmp_lst)
                return
            for x in range(t + 1, n + 1):
                new_lst = copy.copy(tmp_lst)
                dfs(x, new_lst)

        for i in range(1, n + 1):
            dfs(i, [])
        
        return result

# @lc code=end

print(Solution().combine(4, 2))
print(Solution().combine(1, 1))
