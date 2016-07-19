---
layout: leetcode
date: 2016-07-17
title: Super Ugly Number
tags: [Math, Heap]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Write a program to find the n<sup>th</sup> super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list `primes` of size `k`. For example, `[1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]` is the sequence of the first 12 super ugly numbers given `primes` = `[2, 7, 13, 19]` of size `4`.

**Note:**

1. `1` is a super ugly number for any given `primes`.
2. The given numbers in `primes` are in ascending order.
3. 0 < `k` ≤ 100, 0 < `n` ≤ 10<sup>6</sup>, 0 < `primes[i]` < 1000.



***

## CPP Heap Solution

**Result:** Accepted **Time:**  24 ms

Here should be some explanations.

```cpp

int data[1000000+5]={1},cnt;
int value[105],ptr[105];
int nth(int n, int* primes, int primesSize) {
    int ptr[105]={0}, value[105];
    int min_value, last = 1, cnt = 1;
    memcpy(value,primes,sizeof(int)*primesSize);
    while(cnt < n)
    {
        min_value = INT_MAX;
        for(int i = 0; i < primesSize; i++)
        {
            if(value[i] <= last)
                value[i] = primes[i] * data[++ptr[i]];
            if(min_value > value[i])
                min_value = value[i];
        }
        data[cnt++] = last = min_value;
    }
    return data[n-1];
}
class Solution {
public:
    struct cmp{
        bool operator() (const int &a,const int &b) const{ return value[a] > value[b];}
    };
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        
        for(int i = 0; i < primes.size(); i++)
            value[i] = primes[i];
        if(primes.size()*n < 8000480)
            return nth(n,value,primes.size());
        priority_queue<int,vector<int>,cmp> que;
        cnt = 1;
         for(int i = 0; i < primes.size(); i++)
                que.push(i),ptr[i] = 0;
        for(int i = 0; i < n; i++)
        {
            int tmp = que.top();que.pop();
            if(value[tmp] != data[cnt -1])
                data[cnt++] = value[tmp];
            else
                i--;
            value[tmp] = primes[tmp]*data[++ptr[tmp]];
            que.push(tmp);
        }
        return data[n-1];
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n*log(k))$$
- Space Complexity: $$O(n)$$


## C Solution

**Result:** Accepted **Time:**  20 ms


```c
#define MAXN (1000000+5)
int data[MAXN]={1};
int nthSuperUglyNumber(int n, int* primes, int primesSize) {
    int ptr[105]={0}, value[105];
    int min_value, last = 1, cnt = 1;
    memcpy(value,primes,sizeof(int)*primesSize);
    while(cnt < n)
    {
        min_value = INT_MAX;
        for(int i = 0; i < primesSize; i++)
        {
            if(value[i] <= last)
                value[i] = primes[i] * data[++ptr[i]];
            if(min_value > value[i])
                min_value = value[i];
        }
        data[cnt++] = last = min_value;
    }
    return data[n-1];
}

```

**Complexity Analytics**

- Time Complexity: $$O(n*k)$$
- Space Complexity: $$O(n)$$

