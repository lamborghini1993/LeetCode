# -*- coding:utf-8 -*-
"""
@Author: lamborghini
@Date: 2018-12-26 19:54:05
@Desc: LRU缓存机制
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.m_Cap = capacity
        self.m_Cnt = 0
        self.m_Info = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.m_Info:
            val = self.m_Info[key]
            del self.m_Info[key]
            self.m_Info[key] = val
            return val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.m_Info:
            del self.m_Info[key]
            self.m_Info[key] = value
            return
        self.m_Cnt += 1
        self.m_Info[key] = value
        if self.m_Cnt > self.m_Cap:
            for key in self.m_Info:
                del self.m_Info[key]
                return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
