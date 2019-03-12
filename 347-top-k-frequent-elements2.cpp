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
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        map<int, int> q;
        for (int i = 0; i < nums.size(); i++)
            q[nums[i]]++;

        priority_queue<pair<int, int>> p;
        for (auto i = q.begin(); i != q.end(); i++)
            p.push({i->second, i->first});

        vector<int> result;
        for (int i = 0; i < k; i++)
        {
            result.push_back(p.top().second);
            p.pop();
        }
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
