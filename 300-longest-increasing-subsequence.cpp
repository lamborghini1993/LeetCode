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
    int lengthOfLIS(vector<int> &nums)
    {
        int s = nums.size();
        if (s < 1)
            return 0;
        int *dp = new int[s];
        int result;
        result = dp[0] = 1;
        for (int i = 1; i < s; i++)
        {
            dp[i] = 1;
            for (int j = 0; j < i; j++)
            {
                if (nums[i] > nums[j])
                {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            result = max(result, dp[i]);
        }
        return result;
    }
};