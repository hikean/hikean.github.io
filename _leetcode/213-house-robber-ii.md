---
layout: leetcode
date: 2016-07-16
title: House Robber II
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 **Note:** This is an extension of [House Robber](/house-robber/).

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int ret = 0;
        const int sz = nums.size();
        if(sz < 4)
        {
            for(auto x:nums)
                ret = max(x,ret);
            return ret;
        }
        int dp[4]={0,nums[1],nums[2],nums[3]};
        for(int i = 3; i < sz; i++)
            dp[i&3]=nums[i] + max(dp[(i-2)&3],dp[(i-3)&3]);
        ret = max(dp[(sz-1)&3],dp[(sz-2)&3]);
        nums[sz - 1] = 0;
        for(int i = 0; i < 4; i++)
            dp[i] = nums[i];
        dp[2]+= dp[0];
        for(int i = 3; i < sz; i++)
            dp[i&3]=nums[i] + max(dp[(i-2)&3],dp[(i-3)&3]);
        ret = max(ret,max(dp[(sz-1)&3],dp[(sz-2)&3]));
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
