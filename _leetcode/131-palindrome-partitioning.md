---
layout: leetcode
date: 2016-07-13
title: Palindrome Partition
tags: [Backtracking]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>Given a string s, partition s such that every substring of the partition is a palindrome.
>
>Return all possible palindrome partitioning of s.
>
>For example, given s = "aab",
>Return
>
>     [
>       ["aa","b"],
>       ["a","a","b"]
>     ]
>     

***

## Solution

**Result:** Accepted **Time:** 12 ms

Here should be some explanations.

```cpp
class Solution {
public:
    bool is_palindrome(const string & s,int low,int up)
    {
        while(low < up && s[low] == s[--up]) low++;
        return low >= up;
    }
    void dfs(const string s,vector<vector<string>> & ret,vector<string> & vect)
    {
        if(s.empty())
            ret.push_back(vect);
        for(int i = 1 ; i <= s.length(); i++)
            if(is_palindrome(s,0,i))
            {
                vect.push_back(s.substr(0,i));
                dfs(s.substr(i),ret,vect);
                vect.pop_back();
            }
    }
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ret;
        vector<string> vect;
        dfs(s,ret,vect);
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$?
- Space Complexity: $$O(1)$$
