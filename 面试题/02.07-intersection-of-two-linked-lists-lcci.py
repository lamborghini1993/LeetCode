# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-13 17:26:16
"""
https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        tmpA, tmpB = headA, headB
        while tmpA:
            lenA += 1
            tmpA = tmpA.next
        while tmpB:
            lenB += 1
            tmpB = tmpB.next
        if lenA < lenB:
            lenA, lenB = lenB, lenA
            headA, headB = headB, headA
        for _ in range(lenA - lenB):
            headA = headA.next
        ans = headA
        while headA:
            if headA != headB:
                ans = headA.next
            headA, headB = headA.next, headB.next
        return ans
