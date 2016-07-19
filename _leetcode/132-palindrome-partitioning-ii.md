---
layout: leetcode
date: 2016-07-13
title: Palindrome Partitioning II
tags: [Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string s, partition s such that every substring of the partition is a palindrome.
>
>Return the minimum cuts needed for a palindrome partitioning of s.
>
>For example, given s = `"aab"`,
>Return `1` since the palindrome partitioning `["aa","b"]` could be produced using 1 cut.
>
>     

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
#define MAXN 2048
bool dp[MAXN][2]={0};
int cut[MAXN];
int minCut(char* s) {
    const int slen = strlen(s);
    memset(cut,0x3f,sizeof(int)*slen);
    for(int j = 0; j < slen; j++)
        for(int i = 0; i <=j; i++)
        {
            dp[i][j&1] = false;
            if(s[i] == s[j] && (i+1 >= j || dp[(i+1)][(j-1)&1]))
            {
                dp[i][j&1] = true;
                int tmp =  (i?cut[i-1]:0) + 1;
                if(tmp < cut[j])
                    cut[j] = tmp;
            }
        }
    return cut[slen-1]-1;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
