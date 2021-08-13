# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-12 23:15:50
"""
https://leetcode-cn.com/problems/design-linked-list/
"""

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None, None)
        self.num = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.num:
            return -1
        head = self.head
        for _ in range(index + 1):
            head = head.next
        return head.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.num += 1
        node = Node(val, self.head.next)
        self.head.next = node
        self.print()

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.num += 1
        head = self.head
        while head.next:
            head = head.next
        node = Node(val, None)
        head.next = node
        self.print()

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        head = self.head
        for _ in range(index):
            head = head.next
        node = Node(val, head.next)
        head.next = node
        self.num += 1
        self.print()

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.num:
            return
        head = self.head
        for _ in range(index):
            head = head.next
        head.next = None if self.num == (index + 1) else head.next.next
        self.num -= 1
        self.print()

    def print(self):
        head = self.head.next
        print("-" * 20)
        while head:
            print(head.val, end=" -> ")
            head=head.next
        print("[%s]" % self.num)

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(1)
obj.addAtHead(1)
obj.deleteAtIndex(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))

5-2-3-7-2-2-5
