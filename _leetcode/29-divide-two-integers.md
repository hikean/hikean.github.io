---
layout: leetcode
date: 2016-06-26
title: Divide Two Integers
tags: [Math, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Divide two integers without using multiplication, division and mod operator.
>
>If it is overflow, return MAX_INT.
>
>     

***

## Solution

**Result:** Accepted **Time:** 4ms

Here should be some explanations.

```c
int divide(int dv, int dr) {
    if(dv == INT_MIN && dr == -1 || dr == 0)
        return INT_MAX;
    unsigned int tmp = dv,sum = dr,ret = 0,cnt = 1,sign = 1;
    if(tmp & INT_MIN)
        tmp = ~(tmp -1);
    if(sum & INT_MIN)
        sum = ~(sum -1);
    if(tmp < sum)
        return 0;
    unsigned int  ts = sum;
    while(tmp - sum >= sum) sum <<= 1,cnt <<=1;
    while(sum >= ts)
    {
        if(sum <= tmp)
        {
            ret += cnt;
            tmp -= sum;
        }
        sum >>= 1,cnt >>= 1;
    }
    if((dv^dr)&INT_MIN)
        ret = (~ret) + 1;
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
