---
layout: leetcode
date: 2016-06-23
title: Longest Common Prefix
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Write a function to find the longest common prefix string amongst an array of strings.
>

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```c
char* longestCommonPrefix(char** strs, int strsSize) {
    int len=0,maxlen = 4;
    if(strsSize > 0)
        maxlen += strlen(strs[0]);
    char*  ans = (char *) malloc( maxlen*sizeof(char) );
    if(strsSize > 0 )
    while(true)
    {
        if(strs[0][len] == '\0')
            break;
        char tmp = strs[0][len];
        for(int i = 1; i < strsSize; i++)
            if(tmp != strs[i][len])
            {
                ans[len] = '\0';
                return ans;
            }
        ans[len++] = tmp;
    }
    ans[len] = '\0';
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(m*n)$$
- Space Complexity: $$O(n)$$
