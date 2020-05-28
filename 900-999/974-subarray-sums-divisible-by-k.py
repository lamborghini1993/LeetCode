# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-27 19:40:56
@UpdateDate: 2020-05-27 20:30:54
https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/
'''

from typing import List

# ! 超时
# class Solution:
#     def subarraysDivByK(self, A: List[int], K: int) -> int:
#         N = len(A)
#         f = [0] * (N + 1)
#         for i in range(N):
#             tmp = 0
#             for j in range(i, N):
#                 tmp += A[j]
#                 if tmp % K == 0:
#                     f[i] = j - i + 1
#                     break

#         result = 0
#         for i in range(N):
#             temp = i
#             num = 0
#             while temp < N and f[temp]:
#                 num += 1
#                 temp += f[temp]
#             result += num
#         return result


# * 好理解
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans


# ? 没那么好理解
# class Solution:
#     def subarraysDivByK(self, A: List[int], K: int) -> int:
#         record = {0: 1}
#         total = 0
#         for elem in A:
#             total += elem
#             modulus = total % K
#             record[modulus] = record.get(modulus, 0) + 1
        
#         ans = 0
#         for _, cx in record.items():
#             ans += cx * (cx - 1) // 2
#         return ans


func = Solution().subarraysDivByK
print(func([], 3))
print(func([5], 5))
print(func([4, 5, 0, -2, -3, 1], 5))
print(func([4, 5, 0, -2, -3, 1], 3))
