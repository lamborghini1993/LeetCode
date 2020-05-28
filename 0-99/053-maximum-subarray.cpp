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
    int maxSubArray(vector<int> &nums)
    {
        vector<int> dp(nums.size() + 1);
        int result, tmp;
        result = dp[0] = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            dp[i] = max(nums[i], dp[i - 1] + nums[i]);
            result = max(dp[i], result);
        }
        return result;
    }
};

int main()
{
    return 0;
}