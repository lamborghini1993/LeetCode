#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

from typing import List

# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        queue = [(startGene,0)]
        visit = {startGene : True}

        def IsNearStr(Astr:str, Bstr:str) -> bool:
            count = 0
            for i, a in enumerate(Astr):
                if a == Bstr[i]:
                    continue
                count += 1
                if count > 1:
                    return False
            return count == 1

        while queue:
            head, cnt = queue.pop(0)
            if head == endGene:
                return cnt

            for one_bank in bank:
                if one_bank in visit:
                    continue
                if IsNearStr(head, one_bank):
                    queue.append((one_bank, cnt + 1))
                    visit[one_bank] = True
        return -1
# @lc code=end

print(Solution().minMutation(startGene = "AACCGGTT", endGene = "AACCGGTT", bank = ["AACCGGTA"]))
print(Solution().minMutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]))
print(Solution().minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(Solution().minMutation(startGene = "AAAAACCC", endGene = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))

print(Solution().minMutation(startGene = "AACCGGTT", endGene = "AACCGGTC", bank = ["AACCGGTA"]))
