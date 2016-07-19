---
layout: leetcode
date: 2016-07-15
title: Maximum Product Subarray
tags: [Array, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Find the contiguous subarray within an array (containing at least one number) which has the largest product.
>
>For example, given the array `[2,3,-2,4]`,
>the contiguous subarray `[2,3]` has the largest product = `6`.
>
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int m_min(1),m_max(1),ret(INT_MIN);
        for(auto & num : nums){
            int cur_min = std::min(num,std::min(m_min*num,m_max*num));
            int cur_max = std::max(num,std::max(m_min*num,m_max*num));
            ret = std::max(ret,cur_max);
            m_min = cur_min;
            m_max = cur_max;
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
