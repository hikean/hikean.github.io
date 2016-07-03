---
layout: leetcode
date: 2016-06-25
title: Remove Duplicates from Sorted Array
tags: [Array, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
>
>Do not allocate extra space for another array, you must do this in place with constant memory.
>
>For example,
>Given input array `nums = [1,1,2]`,
>
> Your function should return `length = 2`, with the first two elements of nums being `1` and `2` respectively. It doesn't matter what you leave beyond the new length.
>     

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
int removeDuplicates(int* nums, int numsSize) {
    int *top = nums ,*ptr = nums,*last=nums;
    const int  limit = nums + numsSize;
    if(numsSize == 0)
        return 0;
    *(top++) = *(ptr++);
    while(ptr < limit)
    {
        if(*last != *ptr)
            *(top++) = *(ptr);
        ptr++;
        last++;
    }
    return top-nums;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
