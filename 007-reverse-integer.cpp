#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

class Solution
{
  public:
    int min = INT_MIN / 10, max = INT_MAX / 10;
    int reverse(int x)
    {
        int r = 0, tmp;
        while (x != 0)
        {
            tmp = x % 10;
            x = x / 10;
            // 2147483647 -2147483648
            if (r > max || (r == max && tmp > 7))
                return 0;
            if (r < min || (r == min && tmp < -8))
                return 0;
            r = r * 10 + tmp;
        }
        return r;
    }
};

// int main(int argc, const char* argv[])
// {
//     Solution obj = Solution();
//     printf("%d\n", -2 % 10); // C++ 结果为-2
//     printf("%d\n", obj.reverse(123));
//     printf("%d\n", obj.reverse(-123));
//     return 0;
// }
