---
layout: leetcode
date: 2016-06-28
title: Minimum Path Sum
tags: [Array, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a $$m * n$$ grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
>
>**Note:** You can only move either down or right at any point in time.
>
>

***

## Solution

**Result:** Accepted **Time:** 22 ms

Here should be some explanations.

```c
int minPathSum(int** grid, int row, int col) {
    for(int i = 1; i < row; i++)
        grid[i][0]+=grid[i-1][0];
    for(int i = 1; i < col; i++)
        grid[0][i]+=grid[0][i-1];
    for(int r = 1; r < row; r++)
        for(int c = 1; c < col; c++)
            grid[r][c] += grid[r-1][c] < grid[r][c-1] ? grid[r-1][c]:grid[r][c-1];
    return grid[row-1][col-1];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n^2)$$
