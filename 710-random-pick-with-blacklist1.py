import random


class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.m_WhiteList = list(set(range(N)).difference(set(blacklist)))

    def pick(self):
        """
        :rtype: int
        """
        return random.choice(self.m_WhiteList)

# o = Solution(15, [3, 6, 2, 13, 4])
# for x in range(10):
#     print(o.pick())
