---
layout: leetcode
date: 2016-06-28
title: Sqrt(x)
tags: [Binary Search, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Implement `int sqrt(int x)`.
>
>Compute and return the square root of x.
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int mySqrt(int x) {
    int low = 1,up = x;
    while(low < up)
    {
        up  = low + ((up -low) >> 1);
        low = x / up;
    }
    return up;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
