# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-19 17:24:19
@Description: https://leetcode-cn.com/problems/valid-palindrome/
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        def valid(i):
            return i >= 0 and i < len(s)

        def read(i, step):
            while valid(i):
                a: str = s[i]
                if a >= "0" and a <= "9":
                    return i
                if a >= "a" and a <= "z":
                    return i
                i += step
            return i

        l, r = read(0, 1), read(len(s)-1, -1)

        while l < r and valid(l) and valid(r):
            if s[l] != s[r]:
                return False
            l = read(l+1, 1)
            r = read(r-1, -1)
        return True


func = Solution().isPalindrome
print(func(""))
print(func("1"))
print(func("A man, a plan, a canal: Panama"))
print(func("race a car"))
