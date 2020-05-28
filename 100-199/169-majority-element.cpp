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

// class Solution
// {
//     /**
//      * 执行用时: 68 ms, 在Majority Element的C++提交中击败了3.14% 的用户
//      * 内存消耗: 11.4 MB, 在Majority Element的C++提交中击败了0.88% 的用户
//      */
//   public:
//     int majorityElement(vector<int> &nums)
//     {
//         sort(nums.begin(), nums.end());
//         return nums[(nums.size()) / 2];
//     }
// };

class Solution
{
    /**
     * 执行用时: 36 ms, 在Majority Element的C++提交中击败了9.33% 的用户
     * 内存消耗: 11 MB, 在Majority Element的C++提交中击败了0.88% 的用户
     */
  public:
    int result, i, num, tmp;

  public:
    int majorityElement(vector<int> &nums)
    {
        result = nums[0];
        num = 1;
        for (i = 1; i < nums.size(); i++)
        {
            tmp = nums[i];
            if (tmp == result)
            {
                num++;
            }
            else
            {
                num--;
                if (num < 0)
                {
                    num = 1;
                    result = tmp;
                }
            }
        }
        return result;
    }
};