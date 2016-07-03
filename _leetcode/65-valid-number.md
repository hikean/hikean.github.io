---
layout: leetcode
date: 2016-06-28
title: Valid Number
tags: [Math, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Validate if a given string is numeric.
>
>Some examples:
>
>`"0"` => `true`
>
> `" 0.1 "` => `true`
>
> `"abc"` => `false`
>
> `"1 a"` => `false`
>
>`"2e10"` => `true`
>
> **Note:** It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
>

***

## Solution

**Result:** Accepted **Time:** 80 ms

Here should be some explanations.

```python
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip();
        if  len(s) == 0 :
            return False
        try:
            a = float(s)
            return True
        except:
            return False

```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
