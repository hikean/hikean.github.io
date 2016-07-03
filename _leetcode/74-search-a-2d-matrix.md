---
layout: leetcode
date: 2016-06-28
title: Search A 2D Matrix
tags: [Array, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Write an efficient algorithm that searches for a value in an $$m*n$$ matrix. This matrix has the following properties:
>
>  - Integers in each row are sorted from left to right.
>  - The first integer of each row is greater than the last integer of the previous row.
>
>For example,
>Consider the following matrix:
>
>     [
>       [1,   3,  5,  7],
>       [10, 11, 16, 20],
>       [23, 30, 34, 50]
>     ]
>
> Given $$target$$ = `3`, return `true`.
>     

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
bool searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
    register int dx = matrixRowSize - 1,dy = 0,tmp,tar=target;
    while(dy < matrixColSize && dx >= 0)
    {
        tmp = matrix[dx][dy];
        if(tar == tmp) return true;
        if(tar > tmp)
            ++dy;
        else
            --dx;
    }
    return false;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
