#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
#include <algorithm>
#include <stack>
using namespace std;

bool Visit[99999];
int j, cnt;
int result = 0;

class Solution
{
  public:
    int longestValidParentheses(string s)
    {
        stack<int> my;
        cnt = result = 0;

        for (int i = 0; i < s.length(); i++)
        {
            Visit[i] = false;
            if (s[i] == '(')
            {
                my.push(i);
                continue;
            }
            if (!my.empty())
            {
                j = my.top();
                my.pop();
                Visit[j] = true;
                Visit[i] = true;
            }
        }
        for (int i = 0; i < s.length(); i++)
        {
            if (Visit[i])
            {
                cnt++;
                continue;
            }
            result = max(result, cnt);
            cnt = 0;
        }
        result = max(result, cnt);
        printf("结果为:%d\n", result);
        return result;
    }
};

// int main(int argc, char const *argv[])
// {
//     string s1 = ")(";
//     Solution().longestValidParentheses(s1);
//     return 0;
// }