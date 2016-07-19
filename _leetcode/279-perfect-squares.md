---
layout: leetcode
date: 2016-07-17
title: Perfect Squares
tags: [Dynamic Programming, Breadth First Search, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a positive integer n, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to n.

For example, given n = `12`, return `3` because `12 = 4 + 4 + 4`; given n = `13`, return `2` because `13 = 4 + 9`.



***

## Solution


**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
int numSquares(int n) {
    while (n % 4 == 0)
        n /= 4;
    if (n % 8 == 7)
        return 4;
    bool min2 = false;
    for (int i=2; i<=n; ++i) {
        if (i > n/i)
            i = n;
        int e = 0;
        while (n % i == 0)
            n /= i, ++e;
        if (e % 2 && i % 4 == 3)
            return 3;
        min2 |= e % 2;
    }
    return 1 + min2;
}
```

**Result:** Accepted **Time:**  4 ms

```c
#define MAXN (0xffff + 1)
#define INF (0x3fffffff)
#define MAX_CNT (0xffffff)

unsigned int square[MAXN]={0};
int ans[MAX_CNT]={0};

int count(int rest,int power)
{
    if(rest < 4 || power < 2)
        return ans[rest]=rest;
    int ret = power + 5;
    if(rest < MAX_CNT && ans[rest])
        return ans[rest];
    for(int i= power; i > 0 ; i--)
    {
        int rst = rest % square[i];
        int tmp = rest / square[i];
        if(tmp >= ret)
            break;
        tmp += count(rst,sqrt(rst));
        if( tmp < ret)
            ret = tmp;
    }
    return ans[rest]=ret;
}

int numSquares(int n) {
    if(!square[1])
    {
        unsigned int idx = 1;
        for( ; idx < MAXN; idx ++)
            square[idx] = idx * idx;
    }
    return count(n,sqrt(n));
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
