---
layout: leetcode
date: 2016-06-27
title: Pow(x, n)
tags: [Binary Search, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>
> Implement pow(x, n).
>
>

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
double myPow(double x, int n) {
    double ans = 1;
    if(n < 0)
    {
        x = 1.0/x;
        ans = x;
        n = -(n+1);
    }
    while(n)
    {
        if(n&1)
            ans *= x;
        n >>=1;
        x *=x;
    }
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
