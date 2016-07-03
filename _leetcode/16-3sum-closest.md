---
layout: leetcode
date: 2016-06-25
title: 3Sum Closest
tags: [Array, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
>
>      For example, given array S = {-1 2 1 -4}, and target = 1.
>      
>      The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
>

***

## Solution

**Result:** Accepted **Time:** 28ms

Here should be some explanations.

```cpp
class Solution {
    inline int iabs(int a)
    {
        return a > 0 ? a : -a;
    }
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        const int len = nums.size();
        int ret = 0x3fffffff;
        for(int i = 0; i < len - 2; i++)
        {
            int low = i + 1, up = len - 1, diff = nums[i] - target;
            while(low < up)
            {
                int tmp = nums[low] + nums[up] + diff ;
                if(tmp > 0)
                    up --;
                else
                    low ++;
                if(iabs(tmp) < iabs(ret-target))
                    ret = tmp + target;
            }
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n^2$$
- Space Complexity: $$O(1)$$
