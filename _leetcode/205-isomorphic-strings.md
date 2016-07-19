---
layout: leetcode
date: 2016-07-16
title: Isomorphic Strings
tags: [Hash Table]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given two strings s and t, determine if they are isomorphic.<br/>
Two strings are isomorphic if the characters in s can be replaced to get t.<br/>
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

**For example:**<br/>
Given ``"egg"``,``"add"``, return true.<br/>
Given ``"foo"``, ``"bar"``, return false.<br/>
Given ``"paper"``, ``"title"``, return true.

**Note:**<br/>
You may assume both **s** and **t** have the same length.

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
class Solution {
public:
    bool test(const string s,const string t)
    {
        const int len = s.size();
        char m1[256]={0},m2[256]={0};
        const char * ss = s.c_str();
        const char * tt = t.c_str();
        for(int i=0; i<len;i++)
        {
            if(!m1[ss[i]])
                m1[ss[i]] = tt[i];
            else if(m1[ss[i]] != tt[i])
                return false;
            if(!m2[tt[i]])
                m2[tt[i]] = ss[i];
            else if(m2[tt[i]] != ss[i])
                return false;
        }
        return true;
    }
    bool isIsomorphic(string s, string t) {
        return test(s,t) && test(t,s);
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
