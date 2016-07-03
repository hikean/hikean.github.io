---
layout: leetcode
date: 2016-06-25
title: Remove Element
tags: [Array, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an array and a value, remove all instances of that value in place and return the new length.
>
>Do not allocate extra space for another array, you must do this in place with constant memory.
>
>The order of elements can be changed. It doesn't matter what you leave beyond the new length.
>
> **Example:**
>
> Given input array `nums = [3,2,2,3]`, `val = 3`
>
>Your function should return length = 2, with the first two elements of nums being 2.
>     

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
int removeElement(int* nums, int numsSize, int val) {
    int len =0,ptr=-1;
    while(++ptr < numsSize)
    {
        if(nums[ptr] != val)
            nums[len++]=nums[ptr];
    }
    return len;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
