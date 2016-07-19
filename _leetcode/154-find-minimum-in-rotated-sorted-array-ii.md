---
layout: leetcode
date: 2016-07-15
title: Find Minimum in Rotated Sorted Array II
tags: [Array, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Follow up for "Find Minimum in Rotated Sorted Array":
>
>What if duplicates are allowed?
>
> Would this affect the run-time complexity? How and why?
>
> Suppose a sorted array is rotated at some pivot unknown to you beforehand.
>
>(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).
>
>Find the minimum element.
>
>The array may contain duplicates.
>
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int findMin(int* nums, int numsSize) {
    int low = 0,step = numsSize - 1;
    while(step)
    {
        while(low < numsSize -1 && nums[low+1]==nums[low]) low++;
        while(step &&(low + step >= numsSize||nums[low] >= nums[low + step]))
            step >>= 1;
        low += step;
    }
    return nums[(low+1)%numsSize];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
