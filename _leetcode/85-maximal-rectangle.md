---
layout: leetcode
date: 2016-06-28
title: Maximal Rectangle
tags: [Array, Hash Table, Stack, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
>
>  

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int stck[65535],sum[65535];
int largestRectangleArea(int* hgt, int hgtsz) {
    int top = 0,ret = 0;
    for(int i = 0; i <= hgtsz; i ++)
    {
        int now = (i == hgtsz) ? 0:hgt[i];
        while(top && now < hgt[stck[top-1]])
        {
            int h = hgt[stck[--top]];
            int width = (top?i-1 - stck[top-1] : i);
            int tmp = h*width;
            if(tmp > ret)
                ret  = tmp;
        }
        stck[top++] = i;
    }
    return ret;
}
int maximalRectangle(char** matrix, int row, int col) {
    int ret = 0,tmp;
    memset(sum,0,sizeof(int)*col);
    for(int r = 0; r < row; r++)
    {
        for(int c = 0; c < col; c++)
            if(matrix[r][c] == '1')
                sum[c] += 1;
            else sum[c] = 0;
        tmp = largestRectangleArea(sum,col);
        if(tmp > ret)
            ret = tmp;
    }
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
