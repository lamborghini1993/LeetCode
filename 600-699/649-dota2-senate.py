# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-11 15:26:36
"""
https://leetcode-cn.com/problems/dota2-senate/
"""
import collections
from queue import Queue


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"


# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         n = len(senate)
#         r, d = Queue(), Queue()
#         for i, c in enumerate(senate):
#             if c == "R":
#                 r.put(i)
#             else:
#                 d.put(i)

#         while r.qsize() and d.qsize():
#             ri, di = r.get(), d.get()
#             if ri < di:
#                 r.put(ri + n)
#             else:
#                 d.put(di + n)
#         return "Radiant" if r.qsize() else "Dire"


# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         r_num, q = 0, Queue()
#         for c in senate:
#             q.put(c)
#             if c == "R":
#                 r_num += 1
#         diff = 0    # R - D
#         while r_num and r_num != q.qsize():
#             c = q.get()
#             if c == "R":
#                 if diff >= 0:
#                     q.put(c)
#                 elif diff < 0:
#                     r_num -= 1
#                 diff += 1
#             else:
#                 if diff <= 0:
#                     q.put(c)
#                 diff -= 1

#         return "Radiant" if r_num else "Dire"


# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         r_num, q = 0, Queue()
#         for c in senate:
#             q.put(c)
#             if c == "R":
#                 r_num += 1
#         diff = 0    # R - D
#         while r_num and r_num != q.qsize():
#             c = q.get()
#             if diff == 0:
#                 if c == "R":
#                     diff += 1
#                 else:
#                     diff -= 1
#                 q.put(c)
#             elif diff > 0:
#                 if c == "R":
#                     diff += 1
#                     q.put(c)
#                 else:
#                     diff -= 1
#             elif diff < 0:
#                 if c == "R":
#                     diff += 1
#                     r_num -= 1
#                 else:
#                     diff -= 1
#                     q.put(c)

#         return "Radiant" if r_num else "Dire"


func = Solution().predictPartyVictory
print(func("DDDRR"))
print(func("DDRRR"))
print(func("DDRRRR"))
