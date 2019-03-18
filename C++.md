# 二维数组初始化

```c++
int h = 5, w = 8;
char xh[h][w] = {{'1', '1', '1', '1', '1', '1', '1', '1'},
                {'1', '1', '1', '1', '1', '1', '1', '0'},
                {'1', '1', '1', '1', '1', '1', '1', '0'},
                {'1', '1', '1', '1', '1', '0', '0', '0'},
                {'0', '1', '1', '1', '1', '0', '0', '0'}};
// 赋值给vector
vector<vector<char>> matrix;
for (int i = 0; i < h; i++)
{
    vector<char> tmp(xh[i], xh[i] + w);
    matrix.push_back(tmp);
}
```

# 二维vector

```c++
vector<vector<int>> dp(N, vector<int>(M));
```