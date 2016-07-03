---
layout: leetcode
date: 2016-06-28
title: Search in Rotated Sorted Array II
tags: [Array, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Follow up for "Search in Rotated Sorted Array":
>
> What if duplicates are allowed?
>
> Would this affect the run-time complexity? How and why?
>
> Write a function to determine if a given target is in the array.
>
>

***

## Solution

**Result:** Accepted **Time:** 4 ms

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
    while(step && nums[step] == nums[0]) step--;
    while(step)
    {
        while(low + step >= numsSize||nums[low] > nums[low + step])
            step >>= 1;
        low += step;
    }
    if(target >= nums[0])
        return bs(nums,low+1,target) > -1;
    return bs(nums+low+1,numsSize - low-1,target) > -1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Worst Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
