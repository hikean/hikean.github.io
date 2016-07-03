---
layout: leetcode
date: 2016-06-28
title: Remove Duplicates from Sorted Array II
tags: [Array, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> QFollow up for "Remove Duplicates":
>
>What if duplicates are allowed at most twice?
>
>For example,Given sorted array nums = `[1,1,1,2,2,3]`,
>
>Your function should return length = `5`, with the first five elements of nums being `1`, `1`, `2`, `2` and `3`. It doesn't matter what you leave beyond the new length.
>     
>

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int removeDuplicates(int* nums, int numsSize) {
    if(numsSize < 3)
        return numsSize;
    int cnt = 0;
    for(int i = 2; i < numsSize; i++)
        if(nums[i]!=nums[cnt])
            nums[2+cnt++] = nums[i];
    return cnt+2;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
