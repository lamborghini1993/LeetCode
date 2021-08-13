# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-01 09:54:51
@Description: 
https://leetcode-cn.com/problems/bst-sequences-lcci/
'''

import copy
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        result = []

        def dfs(cur: TreeNode, queue: List[int], path: List[int]):
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            if not queue:
                result.append(path)
                return
            for i, nex in enumerate(queue):
                newq = queue[:i] + queue[i + 1:]
                dfs(nex, newq, path + [nex.val])

        dfs(root, [], [root.val])

        return result


def build(lst: List[int]):
    root = TreeNode(lst[0])
    N = len(lst)

    def dfs(node: TreeNode, i: int):
        if not node:
            return
        l = (i << 1) + 1
        r = l + 1
        if l < N:
            left = TreeNode(lst[l])
            node.left = left
            dfs(left, l)
        if r < N:
            right = TreeNode(lst[r])
            node.right = right
            dfs(right, r)

    dfs(root, 0)
    return root


func = Solution().BSTSequences
head = build([1, 2, 3, 4, 5, 6, 7])
print(func(head))
