#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
using namespace std;

class Solution
{
  public:
    // 2147483647 -2147483648
    int min = INT_MIN / 10, max = INT_MAX / 10;
    int myAtoi(string str)
    {
        int r = 0;
        int stautu = 0;
        for (int i = 0; i < str.length(); i++)
        {
            if (r == 0 && str[i] == ' ' && stautu == 0)
                continue;
            else if (r == 0 && stautu == 0 && str[i] == '-')
                stautu = -1;
            else if (r == 0 && stautu == 0 && str[i] == '+')
                stautu = 1;
            else if (str[i] >= '0' && str[i] <= '9')
            {
                int tmp = str[i] - '0';
                // printf("%d", tmp);
                if (r > max || (r == max && tmp > 7))
                    return INT_MAX;
                if (r < min || (r == min && tmp < -8))
                    return INT_MIN;
                r = r * 10 + tmp;
                if (r != 0 && stautu == -1)
                {
                    r = -r;
                    stautu = 3;
                }
            }
            else
                break;
        }
        return r;
    }
};

int main(int argc, const char *argv[])
{
    Solution obj = Solution();
    printf("%d\n", obj.myAtoi("    -42"));
    printf("%d\n", obj.myAtoi("4193 with words"));
    printf("%d\n", obj.myAtoi("words and 987"));
    printf("%d\n", obj.myAtoi("-91283472332"));
    printf("%d\n", obj.myAtoi("- 12 3"));
    printf("%d\n", obj.myAtoi("  -123 sdf34"));
    return 0;
}