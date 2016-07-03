---
layout: leetcode
date: 2016-06-28
title: Edit Distance
tags: [String, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
>
>You have the following 3 operations permitted on a word:
>
>  - Insert a character
>  - Delete a character
>  -  Replace a character
>     

***

## Solution

**Result:** Accepted **Time:** 12 ms

Here should be some explanations.

```c
#define MAXN 2048
int dp[MAXN][MAXN];
int imin(int a,int b)
{
    return  ((a)>(b)?(b):(a));
}
int minDistance(char* a, char* b) {
    const int alen = strlen(a),blen = strlen(b);
    for(int i = 0; i <= alen; i++) dp[i][0] = i;
    for(int j = 1; j <= blen; j++) dp[0][j] = j;
    for(int i = 1; i <= alen; i++)
        for(int j = 1; j <= blen; j++)
            if(a[i-1]==b[j-1])
                dp[i][j] = dp[i-1][j-1];
            else
                dp[i][j] = imin(imin(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])+1;
    return dp[alen][blen];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
