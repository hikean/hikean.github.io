---
layout: leetcode
date: 2016-07-17
title: Word Pattern
tags: [Hash Table]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a `pattern` and a string `str`, find if `str` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `str`.

**Examples:**

1. pattern = "abba", str = "dog cat cat dog" should return true.
2. pattern = "abba", str = "dog cat cat fish" should return false.
3. pattern = "aaaa", str = "dog cat cat dog" should return false.
4. pattern = "abba", str = "dog dog dog dog" should return false.

**Notes:**

You may assume `pattern` contains only lowercase letters, and `str` contains lowercase letters separated by a single space.





***

## Solution

**Result:** Accepted **Time:**  40 ms

Here should be some explanations.

```python
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        cnt = len(words)
        if cnt <> len(pattern):
            return False
        mp1={}
        mp2={}
        for i in xrange(cnt):
            if pattern[i] not in mp1:
                mp1[pattern[i]] = words[i]
            elif mp1[pattern[i]] <> words[i]:
                return False
            if words[i] not in mp2:
                mp2[words[i]] = pattern[i]
            elif mp2[words[i]] <> pattern[i]:
                return False
        return True
        
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
