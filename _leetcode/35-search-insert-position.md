---
layout: leetcode
date: 2016-06-26
title: Search Insert Position
tags: [Array, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
>
> You may assume no duplicates in the array.
>
> Here are few examples.
>
>`[1,3,5,6]`, 5 → 2
>
>`[1,3,5,6]`, 2 → 1
>
>`[1,3,5,6]`, 7 → 4
>
>`[1,3,5,6]`, 0 → 0
>     

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
int searchInsert(int* nums, int numsSize, int target) {
    int low = 0, up = numsSize-1;
    while(low <= up)
    {
        int mid = (low + up) >> 1;
        if(nums[mid] >= target)
            up = mid - 1;
        else
            low = mid + 1;
    }
    return low;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
