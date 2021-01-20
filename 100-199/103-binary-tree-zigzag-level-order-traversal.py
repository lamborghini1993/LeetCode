# -*- coding:utf-8 -*-
# Author: lamborghini1993
# Date: 2020-12-22 10:04:51
"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
"""

from queue import Queue
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        root.index = 0
        q = Queue()
        q.put(root)
        while not q.empty():
            tmp = q.get()
            if tmp.index >= len(result):
                result.append([])
            result[tmp.index].append(tmp.val)

            for node in (tmp.left, tmp.right):
                if not node:
                    continue
                node.index = tmp.index + 1
                q.put(node)
        for i in range(1, len(result), 2):
            result[i] = result[i][::-1]
            # result[i] = list(reversed(result[i]))
            # result[i].reverse()
        return result


root = TreeNode(3)
root.left = TreeNode(9)
tmp = root.right = TreeNode(20)
tmp.left = TreeNode(15)
tmp.right = TreeNode(7)
print(Solution().zigzagLevelOrder(root))
