---
layout: leetcode
date: 2016-06-26
title: Substring with Concatenation of All Words
tags: [Hash Table, Two Pointers, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
>
>For example, given:
>
>**s:** `"barfoothefoobarman"`
>
>**words:** `["foo", "bar"]`
>     
>You should return the indices: `[0,9]`.
>(order does not matter).
>
>

***

## Solution

**Result:** Accepted **Time:** 36ms

Here should be some explanations.

```cpp
#define MAXN 65535
int seq[MAXN],scnt[MAXN],tcnt[MAXN],data[MAXN];
void minWindow(int * s, int slen,int tlen,vector<int> & ret,
    const int start,const int step,const int uni){
    memset(scnt,0,sizeof(int) *(slen +4));
    int i=0,j=0,ucnt = 0;
    while(ucnt < uni && j < slen)
            if(++scnt[s[j]]==tcnt[s[j++]])
                ucnt++;
    if(ucnt == uni)
    while(j <= slen)
    {
        while(scnt[s[i]] > tcnt[s[i]])
             scnt[s[i++]] --;
        if(j-i == tlen)
            ret.push_back(i*step + start);
        scnt[s[j++]]++;
    }
}

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        unordered_map<string,int> mp;
        vector<int> ret;
        int wcnt = 1;
        const int wlen = words[0].length(),lim = s.length() -wlen;
        memset(tcnt,0,sizeof(int) *(words.size()+5));
        for(const auto & x:words)
        {
            if(!mp.count(x))
                mp[x] = wcnt++;
            tcnt[mp[x]] ++;
        }
        for(int i = 0; i <= lim; i++)
        {
            string t = s.substr(i,wlen);
            if(mp.count(t))
                data[i] = mp[t];
            else
                data[i] = 0;
        }
        for(int start = 0; start < wlen; start++)
        {
            int slen = 0;
            for(int i = start; i <= lim; i+=wlen)
                seq[slen++] = data[i];
            minWindow(seq,slen,words.size(),ret,start,wlen,wcnt-1);
        }
        sort(ret.begin(),ret.end());
        return ret;
    }
};

/**
"barfoofoobarthefoobarman"
["bar","foo","the"]

"barfoothefoobarman"
["foo","bar"]

"ababaab"
["ab","ba","ba"]

"wordgoodgoodgoodbestword"
["word","good","best","good"]
**/
```

**Complexity Analytics**

- Time Complexity: $$O(n*k)$$
- Space Complexity: $$O(n)$$
