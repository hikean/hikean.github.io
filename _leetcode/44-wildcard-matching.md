---
layout: leetcode
date: 2016-06-26
title: Wildcard Matching
tags: [Dynamic Programming, Backtracking, Greedy, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Implement wildcard pattern matching with support for `'?'` and `'*'`.
>
>     '?' Matches any single character.
>     '*' Matches any sequence of characters (including the empty sequence).
>     
>     The matching should cover the entire input string (not partial).
>     
>     The function prototype should be:
>     bool isMatch(const char *s, const char *p)
>     
>     Some examples:
>     isMatch("aa","a") → false
>     isMatch("aa","aa") → true
>     isMatch("aaa","aa") → false
>     isMatch("aa", "*") → true
>     isMatch("aa", "a*") → true
>     isMatch("ab", "?*") → true
>     isMatch("aab", "c*a*b") → falseexamples
>     
>     

***

## Solution

**Result:** Accepted **Time:** 144ms

Here should be some explanations.

```c
#define MAXN (4096+512)
bool dp[MAXN][MAXN];
bool isMatch(char* s, char* p) {
    const int m = strlen(s), n  = strlen(p);
    dp[0][0] = true;
    for (int j = 1; j <= n; j++)
        dp[0][j] = dp[0][j-1] && p[j-1] == '*';
    for (int i = 1; i <= m; i++)
            dp[i][0] = false;
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            if (p[j-1] == '?' || s[i-1] == p[j-1])
                dp[i][j] = dp[i-1][j-1];
            else if (p[j-1] == '*')
                dp[i][j] = dp[i-1][j] || dp[i][j-1];
            else
                dp[i][j] = false;
    return dp[m][n];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n^2)$$
