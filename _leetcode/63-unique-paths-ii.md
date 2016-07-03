---
layout: leetcode
date: 2016-06-28
title: Unique Paths II
tags: [Array, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Follow up for "Unique Paths":
>
>Now consider if some obstacles are added to the grids. How many unique paths would there be?
>
>An obstacle and empty space is marked as `1` and `0` respectively in the grid.
>
>For example,
>
>There is one obstacle in the middle of a $$3*3$$ grid as illustrated below.
>
>     [
>       [0,0,0],
>       [0,1,0],
>       [0,0,0]
>     ]  
>
>The total number of unique paths is `2`.
>
>**Note:** m and n will be at most `100`.  

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c

int uniquePathsWithObstacles(int** grid, int row, int col) {
    int dp[105];
    dp[0] = grid[0][0] ^ 1;
    for(int i = 1; i < col; i++)
        dp[i] = grid[0][i] == 1 ? 0 : dp[i-1];
    for(int r = 1 ; r < row; r++)
    {
        if(grid[r][0])
            dp[0] = 0;
        for(int c = 1; c < col; c++)
            if(grid[r][c])
                dp[c] = 0;
            else
                dp[c] += dp[c-1];
    }
    return dp[col-1];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
