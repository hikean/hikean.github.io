---
layout: leetcode
date: 2016-06-23
title: Container with Most Water
tags: [Array, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
>
> Note: You may not slant the container.
>     

***

## Solution

**Result:** Accepted **Time:** 24ms

Here should be some explanations.

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int low = 0, up = height.size() - 1,ret = 0;
        while(low < up)
            if(height[low] < height[up])
                ret = max(height[low]*(up-low),ret),low++;
            else
                ret = max(height[up]*(up-low),ret),up--;
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
