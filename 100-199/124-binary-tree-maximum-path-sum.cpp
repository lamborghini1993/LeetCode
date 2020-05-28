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

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
  public:
    int result = INT_MIN;
    int maxPathSum(TreeNode *root)
    {
        DFS(root);
        return result;
    }

    void DFS(TreeNode *temp)
    {
        int o, a = 0, b = 0;
        o = temp->val;
        if (temp->left)
        {
            DFS(temp->left);
            a = temp->left->val;
        }
        if (temp->right)
        {
            DFS(temp->right);
            b = temp->right->val;
        }
        printf("%d %d %d %d", o, a, b, result);
        // 求最大值
        result = max(result, o);
        result = max(result, o + a);
        result = max(result, o + b);
        result = max(result, o + a + b);
        printf("----%d\n", result);
        // 算出当前节点最大的值
        temp->val = max(o, o + b);
        temp->val = max(temp->val, o + a);
    }
};