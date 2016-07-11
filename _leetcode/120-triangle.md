---
layout: leetcode
date: 2016-07-11
title: Triangle
tags: [Array, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
>
>For example, given the following triangle
>
>     [
>          [2],
>         [3,4],
>        [6,5,7],
>       [4,1,8,3]
>     ]
>     
>The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
>
> **Note:**
>
> Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
>

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int tmin(int** tri,int r,int c,int csz)
{
    if(c+1 >= csz) return tri[r][c];
    if(tri[r][c] > tri[r][c+1])
        return tri[r][c+1];
    return tri[r][c];
}
int minimumTotal(int** tri, int row, int *cols) {
    for(int i = row -2 ; i >= 0 ; i--)
        for(int c = 0; c < cols[i]; c++)
            tri[i][c] += tri[i+1][c] < tri[i+1][c+1]?tri[i+1][c] : tri[i+1][c+1];
    return tri[0][0];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
