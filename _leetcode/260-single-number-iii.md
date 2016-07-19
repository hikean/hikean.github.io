---
layout: leetcode
date: 2016-07-16
title: Single Number III
tags: [Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an array of numbers `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given `nums = [1, 2, 1, 3, 2, 5]`, return ``[3, 5]``.

**Note:**

1. The order of the result is not important. So in the above example, ``[5, 3]`` is also correct.
2. Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?



***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int * ans = malloc(sizeof(int) * 2);
    *returnSize = 2;
    int last_bit = 0, a = 0, b = 0;
    for(int i = 0; i < numsSize; i++)
        last_bit ^= nums[i];
    last_bit = last_bit&(-last_bit);
    for(int i = 0; i < numsSize; i++)
        if(nums[i] & last_bit)
            a ^= nums[i];
        else
            b ^= nums[i];
    ans[0] = a;
    ans[1] = b;
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
