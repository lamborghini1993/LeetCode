# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2021-08-12 21:48:49
"""
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        num = 0
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            num += 1
            if num == k:
                return root.val
            
            root = root.right

        return - 1

    def dfs(self, node):
        left = node.left
        right = node.right
        if left:
            self.dfs(left)
            node.left_num = left.left_num + left.right_num + 1
        else:
            node.left_num = 0
        
        if right:
            self.dfs(right)
            node.right_num = right.left_num + right.right_num + 1
        else:
            node.right_num = 0
        print(node.val, node.left_num, node.right_num)
        
    def kthSmallest_1(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root)

        total, tmp = 0, root
        while tmp:
            rank = total + tmp.left_num + 1
            if rank == k:
                return tmp.val
            if rank > k:
                tmp = tmp.left
            else:
                total += tmp.left_num + 1
                tmp = tmp.right

        return - 1