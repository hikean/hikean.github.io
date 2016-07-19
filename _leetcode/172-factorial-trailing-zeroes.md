---
layout: leetcode
date: 2016-07-16
title: Factorial Trailing Zeroes
tags: [Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an integer n, return the number of trailing zeroes in $$n!$$.

**Note:** Your solution should be in logarithmic time complexity.


***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        int ans = 0;
        while(n)
        {
            n/=5;
            ans +=n;
        }
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
