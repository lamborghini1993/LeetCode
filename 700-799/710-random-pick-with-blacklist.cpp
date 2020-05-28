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
    vector<int> p;
    int size;
    Solution(int N, vector<int> blacklist)
    {
        if (blacklist.size() != 0)
        {
            sort(blacklist.begin(), blacklist.end());
        }
        int j = 0;
        for (int i = 0; i < N; i++)
        {
            while (j < blacklist.size() && blacklist[j] < i)
            {
                j++;
            }
            if(j>=blacklist.size() || blacklist[j]!=i)
                p.push_back(i);
        }
        size = p.size();
        for (int i = 0; i < size; i++)
        {
            printf("%d ",p[i]);
        }
        printf("\n");
    }

    int pick()
    {
        return p[rand() % size];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(N, blacklist);
 * int param_1 = obj.pick();
 */