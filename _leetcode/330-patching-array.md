---
layout: leetcode
date: 2016-07-18
title: Patching Array
tags: [Greedy]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range `[1, n]` inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

**Example 1:**

nums = `[1, 3]`, n = `6`

Return `1`.

Combinations of *nums* are `[1], [3], [1,3]`, which form possible sums of: `1, 3, 4`.
Now if we add/patch `2` to *nums*, the combinations are: `[1], [2], [3], [1,3], [2,3], [1,2,3]`.
Possible sums are `1, 2, 3, 4, 5, 6`, which now covers the range `[1, 6]`.
So we only need `1` patch.

**Example 2:**

nums = `[1, 5, 10]`, n = `20`

Return `2`.

The two patches can be `[2, 4]`.

**Example 3:**

nums = `[1, 2, 2]`, n = `5`

Return `0`.



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
    int minPatches(int* nums, int numsSize, int n)
    {
        int ret = 0,ptr = 0;
        unsigned int range = 0,limit = n;
        while(range < limit)
        {
            if(ptr == numsSize || range + 1 < nums[ptr])
                ++ret,range = (range << 1) | 1;
            else 
                range += nums[ptr++];
        }
        return ret;
    }
    // if you can reach [1,n] ,then you patch n+1 ,you get [1,2n+1].
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
