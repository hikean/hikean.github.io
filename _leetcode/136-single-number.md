---
layout: leetcode
date: 2016-07-13
title: Single Number
tags: [Hash Table, Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an array of integers, every element appears twice except for one. Find that single one.
>
>**Note:**
>
>Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
>
>     

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int singleNumber(int* nums, int numsSize) {
    int ans = 0;
    for(int i = 0; i < numsSize; i++)
        ans ^= nums[i];
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
