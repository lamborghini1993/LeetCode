# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-13 16:43:34
"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs/
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        root = ListNode(0, head)
        first, second = root, head
        while second and second.next:
            next1 = second.next
            next2 = next1.next
            first.next = next1
            next1.next = second
            second.next = next2
            first, second = second, next2
        return root.next

func=Solution().swapPairs
d = ListNode(4)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)
print(func(a))
