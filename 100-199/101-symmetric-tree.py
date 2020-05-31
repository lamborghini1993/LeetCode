# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-05-31 17:44:57
@Description: 
https://leetcode-cn.com/problems/symmetric-tree/
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution: # 递归
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True

#         def same(left: TreeNode, right: TreeNode)->bool:
#             if left is None and right is None:
#                 return True
#             if not (left and right):
#                 return False
#             if left.val != right.val:
#                 return False
#             return same(left.left, right.right) and same(left.right, right.left)

#         return same(root.left, root.right)

class Solution:  # 迭代
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        left, right = root.left, root.right
        queue = []
        queue.append((left, right))
        while queue:
            left, right = queue.pop()
            if left is None and right is None:
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            a1 = (left.left, right.right)
            a2 = (left.right, right.left)
            queue.append(a1)
            queue.append(a2)
        return True
