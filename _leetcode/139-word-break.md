---
layout: leetcode
date: 2016-07-13
title: Word Break
tags: [String, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
>
>For example, given
>
>s = `"leetcode"`,
>
>dict = `["leet", "code"]`.
>
>Return true because `"leetcode"` can be segmented as `"leet code"`.
>
>     

***

## Solution

**Result:** Accepted **Time:** 16 ms

Here should be some explanations.

```cpp
class Solution {
public:
    bool wordBreak(string s, unordered_set<string>& wordDict) {
        const int n = s.length();
        vector<bool> f(n + 1, false);
        f[0] = true;
        for (int i = 1; i <= n; i ++)
            for (int j = 0; j < i; j ++)
                if(f[i] =  f[j] && wordDict.count(s.substr(j, i - j)))
                    break;
        return f[n];
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
