#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
#include <algorithm>
using namespace std;

class Solution
{
  public:
    int result, i;

  public:
    int singleNumber(vector<int> &nums)
    {
        result = 0;
        for (i = 0; i < nums.size(); i++)
        {
            result ^= nums[i];
        }
        return result;
    }
};

int main()
{
}