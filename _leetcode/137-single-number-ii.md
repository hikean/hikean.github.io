---
layout: leetcode
date: 2016-07-13
title: Single Number II
tags: [Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an array of integers, every element appears three times except for one. Find that single one.
>
>**Note:**
>
> Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
>
>     

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int singleNumber(int* nums, int numsSize) {
    long long ans = 0,a,b,pw;
    int i=0;
    for(i = 0; i < numsSize; i++)
    {
        a = ans;
        b = (unsigned int)nums[i];
        ans = 0;
        pw = 1;
        while(a || b)
        {
            ans = ans  + pw*((a+b)%3);
            a/=3;
            b/=3;
            pw *= 3;
        }
    }
    return (unsigned int)ans;

}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
