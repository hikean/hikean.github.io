---
layout: leetcode
date: 2016-06-26
title: First Missing Positive
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an unsorted integer array, find the first missing positive integer.
>
>For example,
>
>Given `[1,2,0]` return `3`,
>
>and `[3,4,-1,1]` return `2`.
>
>Your algorithm should run in $$O(n)$$ time and uses constant space.
>
>

***

## Solution

**Result:** Accepted **Time:** 2ms

Here should be some explanations.

```c
int firstMissingPositive(int* nums, int numsSize) {
        const int n = numsSize;
        for(int i = 0; i < n; i++)
        {
            int tmp = nums[i];
            while( tmp > 0 && tmp <= n)
            {
                if(tmp == nums[tmp-1])
                    break;
                nums[i] = nums[tmp-1];
                nums[tmp-1] = tmp;
                tmp = nums[i];
            }
        }
        for(int i = 0; i < n; i++)
            if(nums[i]!=i+1)
                return i+1;
        return n+1;
    }
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
