---
layout: leetcode
date: 2016-07-11
title: Pascal's Triangle II
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an index k, return the $$k^{th}$$ row of the Pascal's triangle.
>
>For example, given k = 3,
>
>Return `[1,3,3,1]`.
>
>**Note:**
>
>Could you optimize your algorithm to use only O(k) extra space?
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans(rowIndex+1);
        if(rowIndex >= 0)
            ans[0] = 1;
        for(int i = 1; i <= rowIndex; i++)
        {
            int last = 1,now;
            for(int j = 1; j < i; j++)
            {
                now = ans[j-1]+ans[j];
                ans[j-1] = last;
                last = now;
            }
            ans[i-1] = last;
            ans[i] = 1;
        }
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
