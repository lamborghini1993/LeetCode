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
    int l, r, m;
    bool left;
    int search(vector<int> &nums, int target)
    {
        l = 0;
        r = nums.size() - 1;
        while (l <= r)
        {
            m = (l + r) / 2;
            printf("mid %d %d %d\n", l, m, r);
            if (nums[m] == target)
                return m;

            if (nums[l] < nums[r]) // 正常递增
            {
                if (nums[m] > target)
                    r = m - 1;
                else
                    l = m + 1;
            }
            else // 非正常递增
            {
                if (nums[l] <= nums[m]) // 左边是正常递增
                {
                    if (nums[l] <= target && target < nums[m])
                        r = m - 1;
                    else
                        l = m + 1;
                }
                else // 右边是正常递增
                {
                    if (nums[m] < target && target <= nums[r])
                        l = m + 1;
                    else
                        r = m - 1;
                }
            }
        }
        return -1;
    }
};

int main(int argc, char const *argv[])
{
    int t[] = {4, 5, 6, 7, 0, 1, 2};
    vector<int> p;
    int iLen = sizeof(t) / sizeof(t[0]);
    for (int i = 0; i < iLen; i++)
        p.push_back(t[i]);
    cout << Solution().search(p, 2) << endl;
    return 0;
}