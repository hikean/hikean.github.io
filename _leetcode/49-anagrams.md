---
layout: leetcode
date: 2016-06-27
title: Group Anagrams
tags: [String, Hash Table]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an array of strings, group anagrams together.
>
>For example, given: `["eat", "tea", "tan", "ate", "nat", "bat"]`,
>
>Return:
>
>     [
>       ["ate", "eat","tea"],
>       ["nat","tan"],
>       ["bat"]
>     ]
>     
> **Note:** All inputs will be in lower-case.
>

***

## Solution

**Result:** Accepted **Time:** 68 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ret;
        unordered_map<string,multiset<string>> mp;
        for(auto &x:strs)
        {
            auto tmp = x;
            sort(tmp.begin(),tmp.end());
            mp[tmp].insert(x);
        }
        for(auto &x:mp)
            ret.push_back(vector<string>(x.second.begin(),x.second.end()));
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n*k*log(k))$$
- Space Complexity: $$O(n*k)$$
