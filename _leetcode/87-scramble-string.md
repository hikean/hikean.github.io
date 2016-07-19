---
layout: leetcode
date: 2016-06-28
title: Scramble String
tags: [String, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
>
>Below is one possible representation of s1 = `"great"`:
>
>         great
>        /    \
>       gr    eat
>      / \    /  \
>     g   r  e   at
>                / \
>               a   t
>
>To scramble the string, we may choose any non-leaf node and swap its two children.
>
>For example, if we choose the node `"gr"` and swap its two children, it produces a scrambled string `"rgeat"`.
>
>         rgeat
>        /    \
>       rg    eat
>      / \    /  \
>     r   g  e   at
>                / \
>               a   t
>
>We say that `"rgeat"` is a scrambled string of `"great"`.
>
>Similarly, if we continue to swap the children of nodes `"eat"` and `"at"`, it produces a scrambled string `"rgtae"`.
>     
>         rgtae
>        /    \
>       rg    tae
>      / \    /  \
>     r   g  ta  e
>            / \
>           t   a
>
>We say that `"rgtae"` is a scrambled string of `"great"`.
>
>Given two strings s1 and s2 of the same length, determine if s2 is a scrambled >string of s1.
>    

***

## Solution

**Result:** Accepted **Time:** 24 ms

Here should be some explanations.

```c
#define MAXN 512
bool equal[MAXN][MAXN][MAXN]={0};
bool isScramble(char* a, char* b) {
    int alen = strlen(a), blen = strlen(b);
    if(alen != blen)
        return false;
    for(int i = 0; i <= alen; i++)
        for(int j = 0; j <= alen; j++)
            equal[i][j][0] = true,
            equal[i][j][1] = (a[i] == b[j]);
    for(int len = 2, limit = alen - 1; len <= alen; len++, limit-- )
        for(int abgn = 0; abgn < limit; abgn++ )
            for(int bbgn = 0; bbgn < limit; bbgn++ )
            {
                equal[abgn][bbgn][len] = false;
                for(int k = 1; k < len && !equal[abgn][bbgn][len]; k++)
                    equal[abgn][bbgn][len] = equal[abgn][bbgn][len]   ||
                    (equal[abgn + k][bbgn + k][len - k] && equal[abgn][bbgn][k]) ||
                    (equal[abgn][bbgn + k][len - k] && equal[abgn+len-k][bbgn][k]);

            }
    return equal[0][0][alen];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^4)$$
- Space Complexity: $$O(n^3)$$
