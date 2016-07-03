---
layout: leetcode
date: 2016-06-27
title: Jump Game
tags: [Array, Greedy]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>Given an array of non-negative integers, you are initially positioned at the first index of the array.
>
>Each element in the array represents your maximum jump length at that position.
>
>Determine if you are able to reach the last index.
>
> For example:
>
>A = `[2,3,1,1,4]`, return `true`.
>
>A = `[3,2,1,0,4]`, return `false`.

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
bool canJump(int* nums, int numsSize) {
    int des = nums[0];
    for(int i = 0; i < numsSize && des >= i; i++)
        if(nums[i] + i > des)
            des = nums[i] + i;
    return des >= numsSize -1;

}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
