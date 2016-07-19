---
layout: leetcode
date: 2016-07-15
title: Maximum Gap
tags: [Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question



Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.


***

## Solution

**Result:** Accepted **Time:** 16 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int mx = 0;
        sort(nums.begin(),nums.end());
        for(int i = 1; i < nums.size(); i++)
            mx = max(mx,nums[i]-nums[i-1]);
        return mx;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
