---
layout: leetcode
date: 2016-07-16
title: Product of Array Except Self
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an array of n integers where n > 1, `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Solve it **without division** and in $$O(n)$$.

For example, given ``[1,2,3,4]``, return ``[24,12,8,6]``.

**Follow up:**

Could you solve it with constant space complexity? (Note: The output array **does not** count as extra space for the purpose of space complexity analysis.)



***

## Solution

**Result:** Accepted **Time:** 36 ms

Here should be some explanations.

```c
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *ans = malloc(sizeof(int)*numsSize + 8);
    ans[0] = 1;
    for(int i = 1; i < numsSize; i++)
        ans[i] = ans[i-1]*nums[i-1];
    int mul = 1;
    for(int i = numsSize - 2 ; i >= 0 ; i--)
    {
        mul *= nums[i+1];
        ans[i] = ans[i]*mul;
    }
    *returnSize = numsSize;
    return ans;

}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
