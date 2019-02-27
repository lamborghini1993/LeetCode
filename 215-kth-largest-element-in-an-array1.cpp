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
    int i;
    int findKthLargest(vector<int> &nums, int k)
    {
        // 优先队列的内部实现就是用的最小/大堆，所有效率比我们手写快
        priority_queue<int, vector<int>, greater<int>> q;
        for (i = 0; i < k; i++)
            q.push(nums[i]);
        for (i = k; i < nums.size(); i++)
        {
            if (nums[i] > q.top())
            {
                q.pop();
                q.push(nums[i]);
            }
        }
        return q.top();
    }
};

int main()
{
    int t[] = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    int k = 4;
    int len = sizeof(t) / sizeof(t[0]);
    vector<int> nu(t, t + len);
    printf("%d\n", Solution().findKthLargest(nu, k));
    return 0;
}