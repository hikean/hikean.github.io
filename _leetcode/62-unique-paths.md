---
layout: leetcode
date: 2016-06-28
title: Unique Paths
tags: [Array, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
>
>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
>
>How many possible unique paths are there?
>![example](/images/leetcode/62-unique-paths.png)
>Above is a $$3*7$$ grid. How many possible unique paths are there?
>
>**Note:** m and n will be at most 100.
>     

***

## Solution

**Result:** Accepted **Time:** 48 ms

Here should be some explanations.

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        sum = m + n - 2; # c(sum,n-1) = sum!/(n-1)!(m-1)!
        if m < n:
            m,n = n,m
        ans = 1;
        n = 1;
        while m <= sum:
            ans *=m
            ans /= n
            m += 1
            n += 1

        return ans
        
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
