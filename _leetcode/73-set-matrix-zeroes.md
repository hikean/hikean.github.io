---
layout: leetcode
date: 2016-06-28
title: Set Matrix Zeroes
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a $$m*n$$ matrix, if an element is 0, set its entire row and column to 0. Do it in place.
>
>**Follow up:**
>
>Did you use extra space?
>
>A straight forward solution using $$O(mn)$$ space is probably a bad idea.
>
>A simple improvement uses $$O(m + n)$$ space, but still not the best solution.
>
>Could you devise a constant space solution?
>     

***

## Solution

**Result:** Accepted **Time:** 40 ms

Here should be some explanations.

```c
void setZeroes(int** matrix, int matrixRowSize, int matrixColSize) {
    int * row = malloc(sizeof(int) * matrixRowSize);
    int * col = malloc(sizeof(int) * matrixColSize);
    memset(row,0,sizeof(int)* matrixRowSize);
    memset(col,0,sizeof(int)* matrixColSize);
    for(int i = 0; i < matrixRowSize; i++)
        for(int j = 0; j < matrixColSize; j++)
            if(!matrix[i][j])
                row[i] = col[j] = 1;
    for(int i = 0; i < matrixRowSize; i++)
        if(row[i])
            for(int j = 0; j < matrixColSize; j++)
                matrix[i][j] = 0;
    for(int j = 0; j < matrixColSize; j++)
        if(col[j])
            for(int i = 0; i < matrixRowSize; i++)
                matrix[i][j] = 0;
    free(row);
    free(col);
}
```

**Complexity Analytics**

- Time Complexity: $$O(m*n)$$
- Space Complexity: $$O(m+n)$$
