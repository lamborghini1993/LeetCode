#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
#include <algorithm>
#include <set>
#include <unordered_set>
using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        int result = 0;
        unordered_set<int> s(nums.begin(), nums.end());
        for (int val : nums)
        {
            if (!s.count(val))
                continue;
            s.erase(val);
            int pre = val - 1, next = val + 1;
            while (s.count(pre))
                s.erase(pre--);
            while (s.count(next))
                s.erase(next++);
            result = max(result, next - pre - 1);
        }
        return result;
    }
};