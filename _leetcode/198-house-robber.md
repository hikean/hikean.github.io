---
layout: leetcode
date: 2016-07-16
title: House Robber
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int tmp,cur=0,last=0;
        if(!nums.size())
            return 0;
        if(nums.size() == 1)
            return nums[0];
        if(nums.size() == 2)
            return max(nums[0],nums[1]);
        nums[2]+= nums[0];
        for(int i=3;i<nums.size();i++)
            {
                nums[i]+=max(nums[i-2],nums[i-3]);
            }
        return max(nums[nums.size()-1],nums[nums.size()-2]);
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
