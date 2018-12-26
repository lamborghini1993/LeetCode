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

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
  public:
    ListNode *rotateRight(ListNode *head, int k)
    {
        ListNode *tmp = head, *tail;
        int cnt = 0; //  链表长度
        while (tmp)
        {
            cnt++;
            tail = tmp;
            tmp = tmp->next;
        }
        if (cnt == 0)
            return head;
        int t = (cnt - k % cnt) % cnt; // 移动的次数
        if (t == 0)
            return head;
        tail->next = head; // 将链表指向头
        while (t--)
        {
            tmp = head;
            head = head->next;
        }
        tmp->next = NULL;
        return head;
    }
};