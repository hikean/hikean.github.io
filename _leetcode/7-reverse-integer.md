---
layout: leetcode
date: 2016-06-23
title: Reverse Integer
tags: [Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Reverse digits of an integer.
> 
> **Examples:**
>
>     x = 123, return 321
>     x = -123, return -321
>     

***

## Solution

**Result:** Accepted **Time:** 8ms

Here should be some explanations.

```c
int reverse(int x) {
    int flag = 1;
    const int limit = 0x7fffffff / 10 ;
    int ans=0,last = 0;
    if(x < 0)
    {
        flag = -1;
        if(x == 0x80000000)
            return 0;
        x = -x;
    }
    while(x)
    {
        if(last > limit )
            return 0;
        ans= ans*10 + x%10;
        x/=10;
        last = ans;
    }
    return ans*flag;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
