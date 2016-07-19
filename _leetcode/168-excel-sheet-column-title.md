---
layout: leetcode
date: 2016-07-15
title: Excel Sheet Column Title
tags: [Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given a positive integer, return its corresponding column title as appear in an Excel sheet.

 For example:

<pre>
         1 -> A
         2 -> B
         3 -> C
         ...
         26 -> Z
         27 -> AA
         28 -> AB
</pre>
     

***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Solution {
    const string strs[26]={"A","B","C","D","E","F",
                            "G","H","I","J","K","L",
                            "M","N","O","P","Q","R",
                            "S","T","U","V","W","X",
                            "Y","Z"};
public:
    string convertToTitle(int n)
    {
        if(n == 1)
            return "A";
        if(n < 1)
            return "";
        return convertToTitle((n-1)/26) + strs[((n-1)%26)];
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
