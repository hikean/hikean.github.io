---
layout: leetcode
date: 2016-07-13
title: Word Ladder
tags: [String, Breadth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
>
>  1. Only one letter can be changed at a time
>  2. Each intermediate word must exist in the word list
>
> For example,
>
> Given:
>
>beginWord = `"hit"`
>endWord = `"cog"`
>wordList = `["hot","dot","dog","lot","log"]`
>As one shortest transformation is `"hit" -> "hot" -> "dot" -> "dog" -> "cog",`
>return its length `5`.
>
>Note:
>
>  -  Return 0 if there is no such transformation sequence.
>  -  All words have the same length.
>  -  All words contain only lowercase alphabetic characters.
>     

***

## Solution

**Result:** Accepted **Time:** 217 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int ladderLength(string bwrd, string ewrd, unordered_set<string>& list) {
        queue<int> dep;
        queue<string> que;
        que.push(bwrd);dep.push(1);
        list.erase(bwrd);
        while(!que.empty())
        {
            const string tmp = que.front();que.pop();
            const int depth = dep.front();dep.pop();
            if(tmp == ewrd)
                return depth;
            for(int i = 0; i < tmp.length(); i++)
            {
                string str = tmp;
                for(char t = 'a'; t <= 'z'; t++)
                {
                    str[i] = t;
                    if(list.count(str))
                    {
                        que.push(str);
                        list.erase(str);
                        dep.push(depth+1);
                    }
                }
            }
        }
        return 0;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(?)$$
- Space Complexity: $$O(?)$$
