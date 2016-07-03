---
layout: leetcode
date: 2016-06-27
title: Spiral Matrix
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
>
>For example,
>
>Given the following matrix:
>
>     [
>      [ 1, 2, 3 ],
>      [ 4, 5, 6 ],
>      [ 7, 8, 9 ]
>     ]
>     
>You should return `[1,2,3,6,9,8,7,4,5]`.
***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& mat) {

        if(mat.size() < 1 || mat[0].size() < 1) return vector<int>();
        int lx = 0,ly = 0,ux = mat.size(),uy = mat[0].size();
        int x = -1,y = -1,cnt = 0;
        const int limit = ux * uy;
        vector<int> ret(limit);
        while(cnt < limit)
        {
            for(lx++,x++,y++; cnt < limit && y < uy; y++)
                ret[cnt++] = mat[x][y];
            for(uy--,y--,x++; cnt < limit && x < ux; x++)
                ret[cnt++] = mat[x][y];
            for(ux--,x--,y--; cnt < limit && y >= ly; y--)
                ret[cnt++] = mat[x][y];
            for(ly++,y++,x--; cnt < limit && x >= lx; x--)
                ret[cnt++] = mat[x][y];
        }
        return ret;
    }
};

```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
