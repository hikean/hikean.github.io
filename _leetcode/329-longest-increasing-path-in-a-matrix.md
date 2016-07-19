---
layout: leetcode
date: 2016-07-18
title: Longest Increasing Path in a Matrix
tags: [Depth First Search, Topological Sort, Memoization]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

**Example 1:**

<pre>
nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
</pre>

Return `4`

The longest increasing path is `[1, 2, 6, 9]`.

**Example 2:**

<pre>
nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
</pre>

Return `4`

The longest increasing path is `[3, 4, 5, 6]`. Moving diagonally is not allowed.


***

## Solution

**Result:** Accepted **Time:**  28 ms

Here should be some explanations.

```c
#define MAXN 2048
#define zip(x,y) ((x)*(col)+(y))
int max(int a, int b) {return a > b?a:b;}
int dp[MAXN*MAXN];
int dfs(const int x,const int y,const int row,const int col,const int last,const int **mat){
    if(x >= row || y >= col || x < 0 || y < 0 || mat[x][y] <= last)
        return 0;
    int t = zip(x,y);
    if(dp[t]) 
        return dp[t];
    int ret = dfs(x-1,y,row,col,mat[x][y],mat);
    ret = max(ret,dfs(x+1,y,row,col,mat[x][y],mat));
    ret = max(ret,dfs(x,y-1,row,col,mat[x][y],mat));
    ret = max(ret,dfs(x,y+1,row,col,mat[x][y],mat));
    return dp[t] = ++ret;
}
int longestIncreasingPath(int** mat, int row, int col) {
    int ret = 0;
    memset(dp,0,sizeof(int)*zip(row,col));
    for(int i = 0; i < row; i++)
        for(int j = 0; j < col; j++)
                ret = max(ret,dfs(i,j,row,col,mat[i][j] - 1,mat));
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n^2)$$
