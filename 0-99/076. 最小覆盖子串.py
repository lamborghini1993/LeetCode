class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntInfo = {}
        for c in t:
            cntInfo[c] = cntInfo.get(c, 0) + 1

        def isValid():
            for k, v in cntInfo.items():
                if curInfo.get(k, 0) < v:
                    return False
            return True

        minLen, result = len(s) + 1, ""
        curInfo = {}
        left, right = 0, 0
        n = len(s)
        while right < n:
            x = s[right]
            curInfo[x] = curInfo.get(x, 0) + 1

            while isValid():
                if right - left < minLen:
                    minLen = right - left + 1
                    result = s[left : right + 1]

                curInfo[s[left]] -= 1
                left += 1

            right += 1

        return result


obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))
print(obj.minWindow("a", "a"))
print(obj.minWindow("a", "aa"))
