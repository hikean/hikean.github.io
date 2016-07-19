---
layout: leetcode
date: 2016-07-16
title: Maximal Square
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

<pre>1 0 1 0 0
1 0 <font color="red">1</font> <font color="red">1</font> 1
1 1 <font color="red">1</font> <font color="red">1</font> 1
1 0 0 1 0</pre>

Return 4.
     

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
        while(top && now <= hgt[stck[top-1]])
        {
            int h = hgt[stck[--top]];
            int width = (top?i-1 - stck[top-1] : i);
            h =  h > width ? width: h;
            if(h > ret)
                ret  = h;
        }
        stck[top++] = i;
    }
    return ret*ret;
}
int maximalSquare(char** matrix, int row, int col) {
    int ret = 0,tmp;
    memset(sum,0,sizeof(int)*col);
    for(int r = 0; r < row; r++)
    {
        for(int c = 0; c < col; c++)
            sum[c] += (matrix[r][c]=='1'?1:-sum[c]);
        tmp = largestRectangleArea(sum,col);
        if(tmp > ret)
            ret = tmp;
    }
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(1)$$
