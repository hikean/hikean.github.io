---
layout: leetcode
date: 2016-07-11
title: Distinct Subsequences
tags: [String, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string **S** and a string **T**, count the number of distinct subsequences of **T** in **S**.
>
>A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `"ACE"` is a subsequence of `"ABCDE"` while `"AEC"` is not).
>
>Here is an example:
>
>**S** = `"rabbbit"`, **T** = `"rabbit"`
>
>Return `3`.
>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
#define MAXN 1024
int dp[2][MAXN];
void shorter(char *s,char * t)
{
    bool exist[256]={0};
    for(; *t; t++)
        exist[*t] = true;
    char *ptr = s--;
    while(*(++s))
        if(exist[*s])
            *(ptr++) = *s;
    *ptr = 0;
}
int numDistinct(char* s, char* t) {
    shorter(s,t);
    const int slen = strlen(s), tlen = strlen(t);
    dp[0][0] = (s[0]==t[0]);
    for(int i = 1; i < slen; i++)
        dp[0][i] = (s[i] == t[0])+dp[0][i-1];
    if(slen < tlen) return 0;
    for(int r = 1; r < tlen; r++)
    {
        for(int i = 0 ; i < r; i++)
            dp[r&1][i] = 0;
        for(int c = r; c < slen; c++)
            if(t[r]==s[c])
                dp[r&1][c] = dp[(r-1)&1][c-1] + dp[r&1][c-1];
            else
                dp[r&1][c] = dp[r&1][c-1];
    }
    return dp[(tlen-1)&1][slen-1];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
