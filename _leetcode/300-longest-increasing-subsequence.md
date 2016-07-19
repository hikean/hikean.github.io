---
layout: leetcode
date: 2016-07-17
title: Longest Increasing Subsequence
tags: [Dynamic Programming, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given ``[10, 9, 2, 5, 3, 7, 101, 18]``,
The longest increasing subsequence is ``[2, 3, 7, 101]``, therefore the length is `4`. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in $$O(n^2)$$ complexity.

**Follow up:** Could you improve it to *O(n log n)* time complexity?



***

## Solution

**Result:** Accepted **Time:**  36 ms

Here should be some explanations.

```c
int dp[65535];
int lengthOfLIS(int* nums, int nsz) {
    dp[0] = 1;
    int ret = nsz&1;
    for(int i = 1; i < nsz; i++)
    {
        int value = 0;
        for(int j = 0; j < i; j++)
            if(nums[j] < nums[i] && dp[j] > value)
                value = dp[j];
        dp[i] = value+1;
        if(dp[i] > ret)
            ret = dp[i];
    }
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(1)$$
