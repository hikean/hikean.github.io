---
layout: leetcode
date: 2016-07-13
title: Word Break II
tags: [Dynamic Programming, Backtracking, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
>
>Return all such possible sentences.
>
>For example, given
>
>s = `"catsanddog"`,
>
>dict = `["cat", "cats", "and", "sand", "dog"]`.
>
>A solution is `["cats and dog", "cat sand dog"]`.
>     

***

## Solution

**Result:** Accepted **Time:** 40 ms

Here should be some explanations.

```cpp
bool dp[1024][1024]={0};
class Solution {
public:

    void dfs(vector<string> & ret,int cnt,int ptr,const string str,char * buff,
            const int len,const unordered_set<string>& dict)
    {
        for(int i = ptr; i < len; i++)
            {
                buff[cnt++] = str[i];
                buff[cnt] = ' ';
                if(dp[ptr][i] && dict.count(str.substr(ptr,i-ptr+1)))
                {
                    if( i == len -1)
                    {
                        buff[cnt] = 0;
                        ret.push_back(buff);
                        return;
                    }
                    else if(dp[i+1][len-1])
                        dfs(ret,cnt+1,i+1,str,buff,len,dict);
                }
            }
    }
    vector<string> wordBreak(string s, unordered_set<string>& dict) {
        char buff[1024];
        const int len = s.length();
        for(int i = 0 ; i < len ; i++)
            for(int j  = 0,ij=i; ij < len ; j++,ij++)
                {
                    dp[j][ij] = dict.count(s.substr(j,i+1));
                    for(int k = j; k < ij && !dp[j][ij]; k++)
                        dp[j][ij] = dp[j][k] & dp[k+1][ij];
                }
        vector<string> ret;
        dfs(ret,0,0,s,buff,s.length(),dict);
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n^3)$$
- Space Complexity: $$O(n^2)$$
