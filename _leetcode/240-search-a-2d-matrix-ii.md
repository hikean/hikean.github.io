---
layout: leetcode
date: 2016-07-16
title: Search a 2D Matrix II
tags: [Binary Search, Divide and Conquer]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

<pre>
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
</pre>

Given **target** = `5`, return `true`.

Given **target** = `20`, return `false`.





***

## Solution

**Result:** Accepted **Time:** 100 ms

Here should be some explanations.

```c
bool search(int **a, int colnum, int rownum, int k)
{
    if(colnum == 0 || rownum == 0)
        return false;
    int sx = colnum - 1, sy = 0;
    while ( sx >= 0 && sx<colnum && sy >= 0 && sy<rownum)
    {
        if (a[sy][sx]>k)
            --sx;
        else if ( a[sy][sx]<k)
            ++sy;
        else
            return true;
    }
    return false;
}

bool searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
    return search(matrix,matrixColSize, matrixRowSize,target);
}
```

**Complexity Analytics**

- Time Complexity: $$O(n+m)$$
- Space Complexity: $$O(1)$$
