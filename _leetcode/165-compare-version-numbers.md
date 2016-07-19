---
layout: leetcode
date: 2016-07-15
title: Compare Version Numbers
tags: [String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Compare two version numbers version1 and version2.

If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the `.` character.

The `.` character does not represent a decimal point and is used to separate number sequences.

For instance, `2.5` is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

<pre>
     0.1 < 1.1 < 1.2 < 13.37
</pre>     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
int compareVersion(char* version1, char* version2) {
    int v1[500]={0}, v1n = 0;
    int v2[500]={0}, v2n = 0;
    int n1 = 0, n2 = 0;
    while(*version1)
    {
        if(*version1 == '.')
        {
            v1[v1n++] = n1;
            n1 = 0;
        }
        else
        {
            n1 = n1*10 + *version1 - '0';
        }
        ++version1;
    }
    v1[v1n++] = n1;
    while(*version2)
    {
        if(*version2 == '.')
        {
            v2[v2n++] = n2;
            n2 = 0;
        }
        else
        {
            n2 = n2*10 + *version2 - '0';
        }
        ++version2;
    }
    v2[v2n++] = n2;
    int i1=0,i2 =0;
    while(i1 < v1n || i2 < v2n)
    {
        if(v1[i1] > v2[i2])
            return 1;
        else if(v1[i1] < v2[i2])
            return -1;
        ++i1,++i2;
    }
    return 0;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
