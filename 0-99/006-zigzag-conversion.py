class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:    # 特判一下为1的情况
            return s
        result = []
        for i in range(numRows):
            result.append("")
        bUp2Down = False
        for i, c in enumerate(s):
            mod = i % (numRows-1)
            if not mod:
                bUp2Down = not bUp2Down
                
            if bUp2Down:
                result[mod] += c
            else:
                t = numRows-1-mod
                result[t] += c
        r = ""
        for i in range(numRows):
            r += result[i]
            print(result[i])
        return r


Solution().convert("LEETCODEISHIRING", 3)
