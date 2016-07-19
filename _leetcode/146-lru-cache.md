---
layout: leetcode
date: 2016-07-15
title: LRU Cache
tags: [Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `set`.
>
>`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
>
>`set(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
>
>     

***

## Solution

**Result:** Accepted **Time:** 80 ms

Here should be some explanations.

```cpp
#include <iostream>
#include <list>
#include <unordered_map>
using namespace std;
class LRUCache{
private:
    struct LinkNode {
        int key, value;
        LinkNode *next;
        LinkNode(int k, int v, LinkNode* n=NULL):key(k),value(v),next(NULL) {}
        LinkNode():key(0),value(0),next(NULL) {}
    };
    void moveToTail(LinkNode *now) {
        if (now == tail)
            return ;
        LinkNode *tmp = now->next;
        swap(*now,*tmp);
        hash[now->key] = now;
        hash[tmp->key] = tmp;
        if(tmp == tail)
            now->next = tmp;
        else
        {
            tmp->next = NULL;
            tail->next = tmp;
            tail = tmp;
        }
    }

public:
    unordered_map<int, LinkNode *> hash;
    LinkNode Head, *tail,*space;
    int size;

    LRUCache(int capacity):size(capacity){
        tail = &Head;
    }

    int get(int key) {
        if (!hash.count(key))
            return -1;
        moveToTail(hash[key]);
        return hash[key]->value;
    }

    void set(int key, int value) {
        if (hash.count(key)) {
            hash[key]->value = value;
            moveToTail(hash[key]);
            return ;
        }
        if (size > 0)
        {
            space = new LinkNode(key, value);
            size--;
        }
        else
        {
            hash.erase(Head.next->key);
            space = Head.next;
            Head.next = space->next;
            *space = LinkNode(key,value);
        }
        tail->next = space;
        tail =space;
        hash[key] = tail;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
