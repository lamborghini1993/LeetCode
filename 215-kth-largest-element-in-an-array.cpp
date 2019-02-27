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
    int i, j;
    int findKthLargest(vector<int> &nums, int k)
    {
        int *xh = new int[k];
        for (i = 0; i < k; i++)
            xh[i] = nums[i];
        for (i = k / 2; i >= 0; i--)
            CreateHeap(xh, i, k);
        for (i = k; i < nums.size(); i++)
        {
            if (nums[i] > xh[0])
            {
                xh[0] = nums[i];
                CreateHeap(xh, 0, k);
            }
        }
        return xh[0];
    }

    void CreateHeap(int xh[], int root, int n)
    { // 最小顶推
        int left = root * 2 + 1;
        int right, next;
        while (left < n)
        {
            right = left + 1;
            next = left;
            if (right < n && xh[right] <= xh[left])
                next = right;
            if (xh[next] > xh[root])
                break;
            swap(xh[root], xh[next]);
            root = next;
            left = root * 2 + 1;
        }
        // for (int i = 0; i < n; i++)
        // {
        //     printf("%d ", xh[i]);
        // }
        // printf("\n");
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