#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution
{
  public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> num;
        for (auto i : nums)
            num[nums[i]]++;
        
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
