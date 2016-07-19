---
layout: leetcode
date: 2016-07-16
title: Count Primes
tags: [Hash Table, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 **Description:**

 Count the number of prime numbers less than a non-negative number, **n**.

***

## Solution

**Result:** Accepted **Time:** 28 ms

Here should be some explanations.

```cpp

class Solution {
public:
    //const int maxn=100000;
    int countPrimes(int n) {
        bool* bprime  = new bool[n];
        memset(bprime,0,sizeof(bool)*n);
        for(int i=3;i<10000;i+=2)
        {
            if(!bprime[i])
                for(int j = i*i; j < n; j+=i<<1)
                    bprime[j] = 1;
        }
        int ans=1;
        if(n <3)
        ans=0;
        for(int i=3;i<n;i+=2)
            if(!bprime[i])
                ans++;
        delete [] bprime;
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(n)$$
