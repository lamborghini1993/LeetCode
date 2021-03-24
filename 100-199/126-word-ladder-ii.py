# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-06-07 20:01:15
@Description: https://leetcode-cn.com/problems/word-ladder-ii/
WA
'''

from typing import List
from queue import Queue


class Node:
    def __init__(self, word, last=None):
        self.word = word
        self.last = last
        self.step = 0
        if last:
            self.step = last.step + 1


def _left_step(word1, word2):
    cnt = 0
    for i, c in enumerate(word1):
        if c != word2[i]:
            cnt += 1
    return cnt


class Solution:
    """超时，需要构建临界表"""
    def _find_result(self, node, result):
        tmp = []
        while node:
            tmp.insert(0, node.word)
            node = node.last
        result.append(tmp)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set()
        N = len(beginWord)
        for word in wordList:
            if len(word) == N:
                wordSet.add(word)
        if len(endWord) != N or endWord not in wordSet:
            return []
        result = []
        myQueue = Queue()
        myQueue.put(Node(beginWord))
        minStep = 0
        while not myQueue.empty():
            node = myQueue.get()
            word = node.word
            if node.step > len(wordSet):
                continue
            if minStep and minStep < node.step:
                continue
            if word == endWord:
                minStep = node.step
                self._find_result(node, result)
                continue
            for temp in wordSet:
                if _left_step(word, temp) != 1:
                    continue
                myQueue.put(Node(temp, node))
        return result


func = Solution().findLadders
print(func("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(func("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(func("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
