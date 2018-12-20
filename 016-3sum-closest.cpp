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
    int value, minCha = INT_MAX, t;

    void Compare(int tmp, int target)
    {
        t = abs(tmp - target);
        if (t < minCha)
        {
            minCha = t;
            value = tmp;
        }
    }

    int threeSumClosest(vector<int> &nums, int target)
    {
        int i, j, k, tmp;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++)
            cout << nums[i] << " ";
        cout << endl;

        for (i = 0; i < nums.size(); i++)
        {
            j = i + 1;
            k = nums.size() - 1;

            while (j < k)
            {
                tmp = nums[j] + nums[k] + nums[i];
                if (tmp > target)
                {
                    k--;
                    Compare(tmp, target);
                }
                else if (tmp < target)
                {
                    Compare(tmp, target);
                    j++;
                }
                else
                {
                    printf("%d %d %d %d %d\n", i, j, k, tmp, target);
                    return tmp;
                }
            }
        }
        return value;
    }
};

int main(int argc, char const *argv[])
{
    // int t[] = {-1, 2, 1, -4};
    // int iLen = sizeof(t) / sizeof(t[0]);
    // vector<int> p(t, t + iLen);
    // Solution obj = Solution();
    // printf("%d\n", obj.threeSumClosest(p, 1));

    int t[] = {0, 1, 2};
    int iLen = sizeof(t) / sizeof(t[0]);
    vector<int> p(t, t + iLen);
    Solution obj = Solution();
    printf("%d\n", obj.threeSumClosest(p, 3));
    return 0;
}
