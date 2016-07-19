---
layout: leetcode
date: 2016-07-17
title: Maximum Product of Word Lengths
tags: [Bit Manipulation]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a string array `words`, find the maximum value of `length(word[i]) * length(word[j])` where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

**Example 1:**

Given `["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]`

Return `16`

The two words can be `"abcw"`, `"xtfn"`.

**Example 2:**

Given `["a", "ab", "abc", "d", "cd", "bcd", "abcd"]`

Return `4`

The two words can be `"ab"`, `"cd"`.

**Example 3:**

Given `["a", "aa", "aaa", "aaaa"]`

Return `0`

No such pair of words.





***

## Solution

**Result:** Accepted **Time:**  140 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int> vec(words.size());
        for(int i = 0; i < words.size(); i++)
        {
            int mask = 0;
            for(int j = 0; j < words[i].size(); j++)
                mask |= (1 << (words[i][j]-'a'));
            vec[i] = mask;
        }
        int ans = 0,tmp;
        for(int i = 0; i < words.size(); i++)
            for(int j = i + 1; j < words.size(); j++)
                if((vec[i] & vec[j]) == 0)
                    {
                        tmp = words[i].size() * words[j].size();
                        if(tmp > ans)
                            ans = tmp;
                    }
        return ans;
        
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
