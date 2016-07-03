---
layout: leetcode
date: 2016-06-26
title: Generate Parentheses
tags: [Backtracking, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
>
> For example, given n = 3, a solution set is:
>
>     [
>       "((()))",
>       "(()())",
>       "(())()",
>       "()(())",
>       "()()()"
>     ]
>
>     

***

## Solution

**Result:** Accepted **Time:** 0ms

Here should be some explanations.

```cpp
class Solution {
public:
    char str[32]={0};
    void dfs(int left,int right,int cnt,vector<string> & svec)
    {
        if(!right && !left)
           return  svec.push_back(str);
        if(left > 0)
        {
            str[cnt] = '(';
            dfs(left - 1,right,cnt+1,svec);
        }
        if(right > 0 && left < right)
        {
            str[cnt] = ')';
            dfs(left,right-1,cnt+1,svec);
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> svec;
        str[n<<1] = 0;
        dfs(n,n,0,svec);
        return svec;
    }
};

```

**Complexity Analytics**

- Time Complexity: $$O(2^n)$$?
- Space Complexity: $$O(2^n)$$?
