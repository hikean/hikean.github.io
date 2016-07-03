---
layout: leetcode
date: 2016-06-28
title: Simplify Path
tags: [Stack, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an absolute path for a file (Unix-style), simplify it.
>
>For example,
>
>**path** = `"/home/"`, => `"/home"``
>
>**path** = `"/a/./b/../../c/"`, => `"/c"`
>
>**Corner Cases:**
>
>  - Did you consider the case where path = `"/../"`?
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this case, you should return `"/"`.
>
>  - Another corner case is the path might contain multiple slashes `'/'` together, such as `"/home//foo/"`.
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this case, you should ignore redundant slashes and return `"/home/foo"`.
>

***

## Solution

**Result:** Accepted **Time:** 52 ms

Here should be some explanations.

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        lst =[x for x in path.split('/') if x !='.'];
        ret = []
        for x in lst:
            if x == '..':
                if len(ret) > 0:
                    ret.pop()
            elif x:
                ret.append(x)
        return '/'+'/'.join(ret)
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
