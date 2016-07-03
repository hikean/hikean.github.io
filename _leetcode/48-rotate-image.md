---
layout: leetcode
date: 2016-06-27
title: Rotate Image
tags: [Array]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> You are given an $$n*n$$ 2D matrix representing an image.
>
>Rotate the image by 90 degrees (clockwise).
>
>Follow up:
>
>Could you do this in-place?
>


***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
void rotate(int** mat, int rsz, int csz) {
    const int rs = rsz - 1, cs = csz - 1, rs2 = rsz >> 1;
    for(int i = 0, tmp; i < rs2; i++)
        for(int j = i; j < cs - i; j++)
        {
            tmp = mat[i][j];
            mat[i][j] = mat[rs - j][i];
            mat[rs - j][i] = mat[rs - i][cs - j];
            mat[rs - i][cs - j] = mat[j][cs - i];
            mat[j][cs - i] = tmp;
        }
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(1)$$
