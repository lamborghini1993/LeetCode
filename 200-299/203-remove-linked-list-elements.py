# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-12 21:48:49
"""
https://leetcode-cn.com/problems/remove-linked-list-elements/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ans = start = ListNode(None, head)
        while head:
            if head.val == val:
                start.next = head.next
            else:
                start = start.next
            head = head.next
        return ans
