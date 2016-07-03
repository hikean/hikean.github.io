---
layout: leetcode
date: 2016-06-27
title: Maximum Subarray
tags: [Array, Dynamic Programming, Divide and Conquer]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
>
>For example, given the array `[−2,1,−3,4,−1,2,1,−5,4]`,
>the contiguous subarray `[4,−1,2,1]` has the largest `sum = 6`.
>
>**More practice:**
>
>If you have figured out the $$O(n)$$ solution, try coding another solution using the divide and conquer approach, which is more subtle.
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int maxSubArray(int* nums, int numsSize) {
    if(!numsSize)
        return 0;
    int max_sum = nums[0],sum = nums[0];
    for(int i = 1; i < numsSize; i++)
    {
        sum = sum > 0 ? (nums[i] + sum) : (nums[i]);
        max_sum = sum > max_sum ? sum:max_sum;
    }
    return max_sum;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
