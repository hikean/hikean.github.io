---
layout: leetcode
date: 2016-06-23
title: Regular Expression Matching
tags: [Dynamic Programming, Backtracking, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Implement regular expression matching with support for `'.'` and `'*'`.
>
>     '.' Matches any single character.
>     '*' Matches zero or more of the preceding element.
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
>     isMatch("aa", "a*") → true
>     isMatch("aa", ".*") → true
>     isMatch("ab", ".*") → true
>     isMatch("aab", "c*a*b") → true
>     
>     

***

## Solution

**Result:** Accepted **Time:** 20ms

Here should be some explanations.

```c
bool isMatch(char* s, char* p) {
    if(s == NULL || p == NULL)
        return false;
    if(*p==0)
        return *s == 0;
    if(*(p+1) == '*')
        do{
            if(isMatch(s,p+2))
                return true;
        }while(*s && (*p == *(s++) || *p == '.'));
    if(*p == *s || (*p == '.' && *s!=0))
        return isMatch(++s,++p);
    return false;
}
/*
"bbbba"
".*a*a"

"ab"
".*c"

*/
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
