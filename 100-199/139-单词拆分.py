#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0] * (n + 1)

        for i, c in enumerate(s):
            if i != 0 and not dp[i - 1]:
                continue
            for word in wordDict:
                word_len = len(word)
                if s[i : i + word_len] == word:
                    # print(i, word_len, word, i + word_len - 1)
                    dp[i + word_len - 1] = True

        return True if dp[n - 1] else False


# @lc code=end

print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat", "og"]))
print(Solution().wordBreak(s="a", wordDict=["apple", "pen"]))
print(Solution().wordBreak(s="a", wordDict=["a", "pen"]))
print(Solution().wordBreak(s="", wordDict=["a", "pen"]))
