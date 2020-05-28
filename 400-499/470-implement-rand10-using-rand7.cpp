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
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution
{
  public:
    int rand10()
    {
        int t;
        while (true)
        {
            t = (rand7() - 1) * 7 + rand7() - 1;
            if (t < 40)
                return (t + 1) % 10 + 1;
        }
    }
};

