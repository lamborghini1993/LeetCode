#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <map>
#include <climits>
#include <algorithm>
using namespace std;

class Solution
{
  public:
    int i, l, r, m;
    int cnt;

    struct Node
    {
        int x, cnt;
        bool operator<(const Node &a)
        {
            return a.cnt < cnt;
        }
    };

    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        map<int, int, greater<int>> q;
        map<int, int, greater<int>>::iterator it;
        for (i = 0; i < nums.size(); i++)
        {
            m = nums[i];
            it = q.find(m);
            if (it == q.end())
                q[m] = 1;
            else
                (*it).second++;
        }
        Node node[q.size()];
        for (i = 0, it = q.begin(); it != q.end(); it++, i++)
        {
            node[i].x = (*it).first;
            node[i].cnt = (*it).second;
        }
        sort(node, node + i);
        vector<int> result;
        for (i = 0; i < k; i++)
            result.push_back(node[i].x);
        return result;
    }
};

int main()
{
    int t[] = {5, 3, 1, 1, 1, 3, 73, 1};
    int k = 2;
    int len = sizeof(t) / sizeof(t[0]);
    vector<int> nu(t, t + len);
    Solution().topKFrequent(nu, k);
    return 0;
}
