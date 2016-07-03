---
layout: leetcode
date: 2016-06-28
title: Climbing Stairs
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> You are climbing a stair case. It takes n steps to reach to the top.
>
>Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
>     

***

## Solution

**Result:** Accepted **Time:** x ms

Here should be some explanations.

```cpp
class Solution {
    int data[130];
public:
    Solution()
    {
        data[0]=data[1]=1;
        for(int i=2;i<130;i++)
            data[i]= data[i-1]+data[i-2];
    }
    int climbStairs(int n) {
        return data[ n&127];
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
