---
layout: leetcode
date: 2016-07-17
title:  Missing Number
tags: [Array, Math, Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an array containing *n* distinct numbers taken from `0, 1, 2, ..., n`, find the one that is missing from the array.

For example,

Given nums = ``[0, 1, 3]`` return `2`.

**Note:**

Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


***

## Solution

**Result:** Accepted **Time:**  16 ms

Here should be some explanations.

```c
int missingNumber(int* nums, int numsSize) {
    for(int i =  0; i < numsSize; i++)
        nums[i] <<= 1;
    for(int i = 0; i < numsSize; i++)
        nums[nums[i]>>1] |=  1;
    int ans = numsSize ;
    for(int i = 0; i < numsSize; i++)
    {
         if(!(nums[i]&1))
            ans = i;
        nums[i] >>= 1;
    }
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
