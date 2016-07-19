---
layout: leetcode
date: 2016-07-16
title: Bitwise AND of Numbers Range
tags: [Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

***

## Solution

**Result:** Accepted **Time:** 44 ms

Here should be some explanations.

```c
int rangeBitwiseAnd(int m, int n) {
    int ret = 0, tmp = 1, seg = n - m,nm = n&m;
    while(m)
    {
       if(seg < tmp)
            ret |= (nm&tmp);
        tmp <<= 1;
        m >>= 1;
    }
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
