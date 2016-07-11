---
layout: leetcode
date: 2016-07-07
title: Restore IP Addresses
tags: [Backtracking, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string containing only digits, restore it by returning all possible valid IP address combinations.
>
>For example:
>
>Given `"25525511135"`,
>
>return `["255.255.11.135", "255.255.111.35"]`. (Order does not matter)
>
>     

***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```cpp
class Solution {
public:
    void dfs(vector<string> & vect,string str,int ptr,const string s,int lev)
    {
        if(lev >= 4 && ptr >= s.length())
            vect.push_back(str);
        if(ptr >= s.length() || lev >= 4 ) return ;
        int n = s[ptr] - '0';
        char tmp [4]={s[ptr++]},*p;
        p = tmp+1;
        if(lev)
            str += '.';
        while( n <= 255)
            {
                dfs(vect,str+string(tmp),ptr,s,lev+1);
                if(ptr >= s.length() || !n)
                    break;
                *(p++)=s[ptr];
                n = n*10 + s[ptr++]-'0';
            }
    }
    vector<string> restoreIpAddresses(string s) {
        vector<string> vect;
        dfs(vect,"",0,s,0);
        return vect;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
