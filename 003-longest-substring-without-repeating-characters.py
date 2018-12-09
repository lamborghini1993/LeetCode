class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dInfo = {}
        iMax = 0
        iBeginIndex = -1 # 因为下标是从0开始的，所以赋值为-1
        for i, c in enumerate(s):
            if c in dInfo:
                iBeginIndex = max(iBeginIndex, dInfo[c])  #每次维护不重复串的初始下标
            iMax = max(i - iBeginIndex, iMax)
            dInfo[c] = i
        return iMax


def Test():
    """测试样例"""
    lstTest = ["", "abcabvd", "ab", "34f3", "pwwkew", "abba", "abbcccbba", "aabaab!bb"]
    lstResult = [0, 5, 2, 3, 3, 2, 2, 3]
    obj = Solution()
    for i, s in enumerate(lstTest):
        output = obj.lengthOfLongestSubstring(s)
        if lstResult[i] != output:
            print("结果不匹配 Input:%s Output:%s Expected:%s" % (s, output, lstResult[i]))
            break
    print("done")


if __name__ == "__main__":
    Test()
    print(Solution().lengthOfLongestSubstring("aabaab!bb"))
