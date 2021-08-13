# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-13 14:07:21
"""
https://leetcode-cn.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        root = ListNode(None, None)
        while head:
            tmp = head.next
            head.next = root.next
            root.next = head
            head = tmp
        return root.next
