---
layout: leetcode
date: 2016-07-16
title: Majority Element
tags: [Array, Divide and Conquer, Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given an array of size n, find the majority element. The majority element is the element that appears **more than** `⌊ n/2 ⌋` times.

You may assume that the array is non-empty and the majority element always exist in the array.


***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int majorityElement(int* nums, int numsSize) {
    int ans = nums[0],cnt = 1,i =1;
    for(;i < numsSize; i++)
    {
        cnt += (ans == nums[i] ? 1:-1);
        if(!cnt)
        {
            ans = nums[i];
            cnt = 1;
        }
    }
    return ans;

}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
