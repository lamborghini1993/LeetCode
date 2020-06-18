# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-18 14:23:32
@Description: 
https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None

        index = 0
        last_layer = 0

        def read_num() -> int:
            nonlocal index
            num = 0
            while index < len(S) and S[index] != "-":
                num = num * 10 + int(S[index])
                index += 1
            return num

        def read_layer() -> int:
            nonlocal index
            num = 0
            while index < len(S) and S[index] == "-":
                num += 1
                index += 1
            return num

        def read_node(layer: int):
            nonlocal last_layer
            if last_layer:
                cur_layer = last_layer
            else:
                cur_layer = read_layer()
            if cur_layer == layer + 1:
                last_layer = 0
                return True
            last_layer = cur_layer
            return False

        def dfs(node: TreeNode, layer: int):
            if index >= len(S):
                return
            has_left = read_node(layer)
            if has_left:
                node.left = TreeNode(read_num())
                dfs(node.left, layer + 1)
            has_right = read_node(layer)
            if has_right:
                node.right = TreeNode(read_num())
                dfs(node.right, layer + 1)

        root = TreeNode(read_num())
        dfs(root, 0)
        return root


func = Solution().recoverFromPreorder
print(func(""))
print(func("1"))
print(func("1-2--3--4-5--6--7"))
print(func("1-2--3---4-5--6---7"))
print(func("1-401--349---90--88"))
