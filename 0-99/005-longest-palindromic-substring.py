class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "#" + "#".join(s) + "#"
        RL = [0] * len(s)
        maxRight = 0
        pos = 0
        maxLen = 0
        maxIndex = 0
        for i in range(len(s)):
            if i < maxRight:
                RL[i] = min(RL[2*pos-i], maxRight-i)
            else:
                RL[i] = 1
            while i-RL[i] >= 0 and i+RL[i] < len(s):
                l = s[i-RL[i]]
                r = s[i+RL[i]]
                if l != r:
                    break
                RL[i] += 1
            if RL[i] + i - 1 > maxRight:
                maxRight = RL[i]
                pos = i
            if RL[i] > maxLen:
                maxLen = RL[i]
                maxIndex = i
        p = s[maxIndex-maxLen+1:maxIndex+maxLen-1]
        return p.replace("#", "")


Solution().longestPalindrome("babad")
