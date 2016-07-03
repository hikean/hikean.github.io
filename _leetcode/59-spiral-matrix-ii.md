---
layout: leetcode
date: 2016-06-28
title: Spiral Matrix II
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an integer n, generate a square matrix filled with elements from $$1$$ to $$n^2$$ in spiral order.
>
>For example,
>
>Given $$n = 3$$,
>
>You should return the following matrix:
>
>     [
>      [ 1, 2, 3 ],
>      [ 8, 9, 4 ],
>      [ 7, 6, 5 ]
>     ]
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int lx = 0,ly = 0,ux = n,uy = n;
        int x = -1,y = -1,cnt = 0;
        const int limit = ux * uy;
        vector<vector<int>> ret(ux,vector<int>(uy));
        while(cnt < limit)
        {
            for(lx++, x++, y++; cnt < limit && y < uy; y++)
                ret[x][y] = ++cnt;
            for(uy--, y--, x++; cnt < limit && x < ux; x++)
                ret[x][y] = ++cnt;
            for(ux--, x--, y--; cnt < limit && y >= ly; y--)
                ret[x][y] = ++cnt;
            for(ly++, y++, x--; cnt < limit && x >= lx; x--)
                ret[x][y] = ++cnt;
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
