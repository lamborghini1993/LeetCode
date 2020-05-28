class Solution:
    m_Min = -2**31
    m_Max = 2**31 - 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            str_x = str(abs(x))
            x = "-"
        else:
            str_x = str(x)
            x = ""
        x += str_x[::-1]
        result = int(x)
        print(self.m_Max, self.m_Min)
        if result < self.m_Min or result > self.m_Max:
            return 0
        return result


print(-2 % 10)    # python结果为8
Solution().reverse(123)
Solution().reverse(-123)
