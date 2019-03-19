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

bool Compare(const pair<int, int> &a, const pair<int, int> &b)
{
    // 比较函数需要是静态方法，所有必须放到类的外面
    // 先按照第一个元素从小到大排序，在按照第二个元素从小到大排序
    if (a.first == b.first)
        return a.second < b.second;
    return a.first < b.first;
}

class Solution
{
  public:
    int maxEnvelopes(vector<pair<int, int>> &envelopes)
    {
        if (envelopes.size() < 1)
            return 0;
        int result;
        sort(envelopes.begin(), envelopes.end(), Compare);
        // for (auto x : envelopes)
        //     printf("%d %d\n", x.first, x.second);
        vector<int> dp(envelopes.size());
        result = 0;
        for (int i = 0; i < envelopes.size(); i++)
        {
            dp[i] = 1;
            for (int j = 0; j < i; j++)
            {
                if (envelopes[i].first > envelopes[j].first && envelopes[i].second > envelopes[j].second)
                    dp[i] = max(dp[i], dp[j] + 1);
            }
            result = max(result, dp[i]);
        }
        return result;
    }
};

int main()
{
    return 0;
}