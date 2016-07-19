---
layout: leetcode
date: 2016-07-16
title: Number of Islands
tags: [Depth First Search, Breadth First Search, Union Find]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

<pre>
     11110
     11010
     11000
     00000

</pre>

Answer: **1**

**Example 2:**

<pre>
     11000
     11000
     00100
     00011
</pre>

Answer: **3**



***

## Solution

**Result:** Accepted **Time:** 116 ms

Here should be some explanations.

```c
bool vis[4096][4096]={0};

int dfs(char ** grid,int x,int y,const int r,const int c)
{
    if(x < 0 || y < 0 || x >= r || y >= c)
        return 0;
    if(grid[x][y] == '0' || vis[x][y])
    return 0;
    vis[x][y] = 1;
    dfs(grid,x+1,y,r,c);
    dfs(grid,x-1,y,r,c);
    dfs(grid,x,y-1,r,c);
    dfs(grid,x,y+1,r,c);

    return 1;
}

int numIslands(char** grid, int gridRowSize, int gridColSize) {
    memset(vis,0,sizeof(vis));
    int ret = 0;
    for(int x = 0; x < gridRowSize; x ++)
    for(int y = 0; y < gridColSize; y ++)
        ret += dfs(grid,x,y,gridRowSize,gridColSize);
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
