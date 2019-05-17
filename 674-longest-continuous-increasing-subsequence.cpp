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
    int findLengthOfLCIS(vector<int> &nums)
    {
        if (nums.size() == 0)
            return 0;
        int result = 0, cnt = 0, temp = INT32_MIN;
        for (int i = 0; i < nums.size(); i++)
        {
            if (temp >= nums[i])
            {
                result = max(cnt, result);
                cnt = 1;
            }
            else
            {
                cnt++;
            }
            temp = nums[i];
        }
        result = max(cnt, result);
        return result;
    }
};