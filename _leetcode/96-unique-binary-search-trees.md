---
layout: leetcode
date: 2016-07-11
title: Unique Binary Search Trees
tags: [Tree, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


> Given an integer n, how many structurally  unique **BST**'s (binary search trees) that store values 1...n.
>
>For example,
>
>Given n = 3, your program should return all 5 unique BST's shown below.
>
>         1         3     3      2      1
>          \       /     /      / \      \
>           3     2     1      1   3      2
>          /     /       \                 \
>         2     1         2                 3
>     


***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
#define MAXN 256
int bst[MAXN]={0};
int numTrees(int n) {
    if(!bst[0])
    {
        bst[0] = 1;
        for(int k = 1; k < MAXN; k++)
            for(int  i= 0; i < k; i++)
                bst[k] += bst[i] * bst[k-1-i];
    }
    return bst[n];
}
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(n)$$
