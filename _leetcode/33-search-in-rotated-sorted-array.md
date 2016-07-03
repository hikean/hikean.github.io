---
layout: leetcode
date: 2016-06-26
title: Search in Rotated Sorted Array
tags: [Array, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Suppose a sorted array is rotated at some pivot unknown to you beforehand.
>
> (i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).
>
>You are given a target value to search. If found in the array return its index, otherwise return -1.
>
>You may assume no duplicate exists in the array.
>
>     

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
int bs(int *nums,int sz,int target)
{
    int low = 0,up = sz-1,mid;
    while(low <= up)
    {
        mid = (low + up) >> 1;
        if(nums[mid] > target)
            up = mid -1;
        else if(nums[mid] < target)
            low = mid + 1;
        else
            return mid;
    }
    return -1;
}

int search(int* nums, int numsSize, int target) {
    int low = 0,step = numsSize - 1;
    while(step)
    {
        while(low + step >= numsSize||nums[low] > nums[low + step])
            step >>= 1;
        low += step;
    }
    if(target >= nums[0])
        return bs(nums,low+1,target);
    int ret = bs(nums+low+1,numsSize - low-1,target);
    return ret == -1 ? -1 : ret + low + 1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
