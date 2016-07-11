---
layout: leetcode
date: 2016-07-07
title: Decode Ways
tags: [Dynamic Programming, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> A message containing letters from A-Z is being encoded to numbers using the following mapping:
>
>     'A' -> 1
>     'B' -> 2
>     ...
>     'Z' -> 26
>     
>Given an encoded message containing digits, determine the total number of ways to decode it.
>
>For example,
>
>Given encoded message `"12"`, it could be decoded as `"AB"` (1 2) or `"L"` (12).
>
>The number of ways decoding `"12"` is 2.


***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c

int dp[1000][2]={0};
int numDecodings(const char * str)
{
    int sum = 0,i;
    if(str == NULL || str[0] == 0 || str[0] == '0')
        return 0;
    dp[0][1]=0;
    dp[0][0]=1;
    dp[1][0]=1;
    dp[1][1]=0;
    for(i=1;str[i];i++)
    {
        sum = (str[i-1]&0xf)*10 + (str[i]&0xf);
        if(str[i] != '0')
            dp[i+1][0] = dp[i][0] + dp[i][1];
        else
            dp[i+1][0] = 0;
        if(sum > 9 && sum <= 26)
            dp[i+1][1] = dp[i-1][0] + dp[i-1][1];
        else dp[i+1][1] = 0;
    }
    return dp[i][0] + dp[i][1];
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
