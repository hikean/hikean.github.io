---
layout: leetcode
date: 2016-07-15
title: Find Minimum in Rotated Sorted Array
tags: [Array, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>
> Suppose a sorted array is rotated at some pivot unknown to you beforehand.
>
>(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).
>
>Find the minimum element.
>
>You may assume no duplicate exists in the array.
>
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
int findMin(int* nums, int numsSize) {
    int low = 0,step = numsSize - 1;
    while(step)
    {
        while(low + step >= numsSize||nums[low] > nums[low + step])
            step >>= 1;
        low += step;
    }
    return nums[(low+1)%numsSize];
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
