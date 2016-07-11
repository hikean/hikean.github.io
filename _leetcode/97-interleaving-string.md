---
layout: leetcode
date: 2016-07-11
title: Interleaving String
tags: [String, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
>
>For example,
>
>Given:
>
>s1 = `"aabcc"`,
>
>s2 = `"dbbca"`,
>
>When s3 = `"aadbbcbcac"`, return true.
>
>When s3 = `"aadbbbaccc"`, return false.
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
bool dp[2048][2048];
bool isInterleave(char* a, char* b, char* c) {
    const int alen = strlen(a),blen = strlen(b),clen = strlen(c);
    if(alen + blen != clen)
        return false;
    dp[0][0] = true;
    for(int i = 1; i <= clen; i++){
        dp[0][i] = (dp[0][i-1] && c[i-1]==b[i-1]);
        dp[i][0] = (dp[i-1][0] && c[i-1]==a[i-1]);
        for(int j = i > alen ? i - alen:1; j < i && j <= blen; j++)
            dp[i-j][j] = (dp[i-j][j-1] && c[i-1] == b[j-1])||(dp[i-j-1][j] && c[i-1] == a[i-j-1]);
    }
    return dp[alen][blen];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n^2)$$
