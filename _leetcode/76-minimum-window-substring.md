---
layout: leetcode
date: 2016-06-28
title: Minimum Window Substring
tags: [Hash Table, Two Pointers, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string **S** and a string **T**, find the minimum window in **S** which will contain all the characters in **T** in complexity $$O(n)$$.
>
>For example,
>
> **S** = `"ADOBECODEBANC"`
>
> **T** = `"ABC"`
>
> Minimum window is `"BANC"`.
>
> **Note:**
>
>If there is no such window in **S** that covers all characters in **T**, return the empty string `""`.
>
> If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in **S**.
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
char* minWindow(char* s, char* t) {
    int scnt[256]={0},tcnt[256]={0},reti=0,retj=INT_MAX,i=0,j=0,uni = 0,ucnt = 0;
    const int slen = strlen(s);
    for(char * x = t;  *x; x++)
        if(++tcnt[*x] == 1)
            uni++;
    while(ucnt < uni && j < slen)
            if(++scnt[s[j]]==tcnt[s[j++]])
                ucnt++;
    if(ucnt == uni)
    while(j <= slen)
    {
        while(scnt[s[i]] > tcnt[s[i]])
             scnt[s[i++]] --;
        if(j-i < retj - reti)
            reti= i,retj=j;
        scnt[s[j++]]++;
    }
    if(retj == INT_MAX)
        return s+slen;
    s[retj]=0;
    return s+reti;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
