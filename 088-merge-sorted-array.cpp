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
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int i = m - 1, j = n - 1;
        while (i >= 0 && j >= 0)
        {
            if (nums1[i] > nums2[j])
            {
                nums1[i + j + 1] = nums1[i];
                i--;
            }
            else
            {
                nums1[i + j + 1] = nums2[j];
                j--;
            }
        }
        if (j >= 0)
            for (int t = j; t >= 0; t--)
                nums1[t] = nums2[t];
    }
};