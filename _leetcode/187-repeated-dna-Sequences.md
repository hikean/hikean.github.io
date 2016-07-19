---
layout: leetcode
date: 2016-07-16
title: Repeated DNA Sequences
tags: [Hash Table, Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: `"ACGAATTCCG"`. When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

 Write a function to find all the 10-letter-long sequences (substrings) that > occur more than once in a DNA molecule.

 For example,

Given s = ``"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"``,

Return: ``["AAAAACCCCC", "CCCCCAAAAA"]``.

***

## Solution

**Result:** Accepted **Time:** 136 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int chrs[256]={0};
    int get_value(const string s)
    {
        int ret = 0;
        for(const auto x:s)
            ret = (ret<<2)|chrs[x];
        return ret;
    }
    vector<string> findRepeatedDnaSequences(string s) {
        chrs['A'] = 0;
        chrs['C'] = 1;
        chrs['G'] = 2;
        chrs['T'] = 3;
        unordered_map<int,int> mp;
        vector<string> ret;
        const int limit = int(s.length()) - 9;
        for(int i = 0; i < limit; i++)
        {
            string tmp = s.substr(i,10);
            int value = get_value(tmp);
            mp[value]++;
            if(mp[value] == 2)
                ret.push_back(tmp);
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
