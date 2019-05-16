import random


class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.m_Map = {}
        self.m_Size = N-len(blacklist)
        replace = N-1
        # 建立黑名单中的替代路径
        for n in blacklist:
            self.m_Map.setdefault(n, replace)
            replace -= 1

        # 路径压缩
        for n in blacklist:
            if n >= self.m_Size:
                continue
            if n in self.m_Map:
                nxt = self.m_Map[n]
                while nxt in self.m_Map:
                    nxt = self.m_Map[nxt]
                self.m_Map[n] = nxt

    def pick(self):
        """
        :rtype: int
        """
        rd = int(random.random()*self.m_Size)
        return self.m_Map.get(rd, rd)


# o = Solution(15, [3, 6, 2, 13, 4])
# for x in range(10):
#     print(o.pick())
