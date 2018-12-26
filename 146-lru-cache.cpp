#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <climits>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <list>
using namespace std;

class LRUCache
{
  public:
    struct _node
    {
        int _key;
        int _val;
        _node(int k, int v) : _val(v), _key(k){};
    };

  public:
    list<_node> _list;
    unordered_map<int, list<_node>::iterator> keynode;
    int _maxsize;
    int _cursize;
    LRUCache(int capacity)
    {
        _maxsize = capacity;
        _cursize = 0;
    }

    int get(int key)
    {
        if (_cursize == 0)
        {
            return -1;
        }
        if (keynode.find(key) != keynode.end())
        {
            int res = keynode[key]->_val;
            _list.erase(keynode[key]);
            _list.push_front(_node(key, res));
            keynode[key] = _list.begin();
            return res;
        }
        return -1;
    }

    void put(int key, int value)
    {
        if (keynode.find(key) != keynode.end())
        {
            _list.erase(keynode[key]);
            _list.push_front(_node(key, value));
            keynode[key] = _list.begin();
            return;
        }
        _cursize++;
        if (_cursize <= _maxsize)
        {
            _list.push_front(_node(key, value));
            keynode[key] = _list.begin();
        }
        else
        {
            _list.push_front(_node(key, value));
            int rkey = (--_list.end())->_key;
            keynode.erase(rkey);
            keynode[key] = _list.begin();
            _list.pop_back();
        }
    }
};