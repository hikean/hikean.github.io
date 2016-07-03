---
layout: leetcode
date: 2016-06-25
title: Longest Valid Parentheses
tags: [String, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.
>
>For `"(()"`, the longest valid parentheses substring is `"()"`, which has `length = 2`.
>
>Another example is `")()())"`, where the longest valid parentheses substring is `"()()"`, which has `length = 4`.
>
>

***

## Solution

**Result:** Accepted **Time:** 12ms

Here should be some explanations.

```c
#define MAXN (60048)
int stck[MAXN],dp[MAXN];
int longestValidParentheses(char* s) {
    int ans = 0, top = 0;
    for(int i = 0; s[i]; i++)
    {
        dp[i] = 0;
        if(s[i] == '(')
            stck[top++] = i;
        else if(top)
        {
            int tmp = stck[--top];
            dp[i] = i - tmp + 1 + (tmp?dp[tmp-1]:0);
            ans = ans < dp[i]?dp[i]:ans;
        }
    }
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
