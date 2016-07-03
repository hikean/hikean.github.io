---
layout: leetcode
date: 2016-06-27
title: N-Queens
tags: [Hash Table, Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Follow up for N-Queens problem.
>
>Now, instead outputting board configurations, return the total number of distinct solutions.
>![N Queens](/images/leetcode/51-n-queens.png)
>
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
void dfs(int row,const int n,int *col,int*xy,int*yx,int *ans){
    *ans = *ans + (row == n);
    for(int i = 0; i < n && row < n;i++)
        if(!col[i] && !xy[n + row - i] && !yx[row + i])
            dfs(row + (col[i] = xy[n + row - i] = yx[ row + i] = 1),n,col,xy,yx,ans),
            col[i] = xy[n + row - i] = yx[ row + i] = 0;
}
int totalNQueens(int n) {
    int col[64]={0},xy[64]={0},yx[64]={0},ans=0;
    dfs(0,n,col,xy,yx,&ans);
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n!)$$
- Space Complexity: $$O(1)$$
