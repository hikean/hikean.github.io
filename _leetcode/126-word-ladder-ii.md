---
layout: leetcode
date: 2016-07-13
title: Word Ladder II
tags: [Array, Backtracking, Breadth First Search, String]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
>
>  -  Only one letter can be changed at a time
>  -  Each intermediate word must exist in the word list
>
>For example,
>
>Given:
>
> beginWord = `"hit"`
> endWord = `"cog"`
> wordList = `["hot","dot","dog","lot","log"]`
>
> Return
>
>       [
>         ["hit","hot","dot","dog","cog"],
>         ["hit","hot","lot","log","cog"]
>       ]
>
> **Note:**
>  -  All words have the same length.
>  - All words contain only lowercase alphabetic characters.
>   

***

## Solution

**Result:** Accepted **Time:** 1142 ms

Here should be some explanations.

```cpp
class Solution {
public:
    void dfs(const int limit,int depth,
    vector<vector<string>> & ret,
    vector<string> &vect,
    unordered_set<string> & st,
    const string eword,const string last,
     unordered_map<string,set<string>> & father)
    {
        if(depth >= limit || !father.count(last))
            return;
        for(const string & str : father[last])
        {
            if(str == eword)
            {
                ret.push_back(vect);
                ret.back().push_back(str);
                reverse(ret.back().begin(),ret.back().end());
            }
            else if(!st.count(str))
            {
                st.insert(str);
                vect.push_back(str);
                dfs(limit,depth+1,ret,vect,st,eword,str,father);
                vect.pop_back();
                st.erase(str);
            }
        }
    }
    vector<vector<string>> findLadders(string beginWord, string endWord, unordered_set<string> &wordList) {
        vector<vector<string>> ret;
        vector<string> vect;
        unordered_set<string> st;
        unordered_map<string,set<string>> father;
        vect.push_back(endWord);
        st.insert(endWord);
        int limit = ladderLength(beginWord,endWord,wordList,father);
        dfs(limit,1,ret,vect,st,beginWord,endWord,father);
        return ret;
    }
    int ladderLength(string bwrd, string ewrd,
    unordered_set<string> list,
   unordered_map<string,set<string>> & father) {
        queue<string> que;
        que.push(bwrd);
        que.push("");
        int depth = 1;
        bool flag = true;
        while(!que.empty() && flag)
        {
            string tmp = bwrd;
            set<string> tset;
            while(true){
                tmp = que.front();que.pop();
                list.erase(tmp);
                if(tmp == "")
                {
                    depth ++;
                    break;
                }
                else if(tmp == ewrd)
                    flag = false;
                else
                {
                    for(int i = 0; i < tmp.length(); i++)
                    {
                        string str = tmp;
                        for(char t = 'a'; t <= 'z'; t++)
                        {
                            str[i] = t;
                            if(list.count(str))
                            {
                                que.push(str);
                                tset.insert(str);
                                father[str].insert(tmp);
                            }
                        }
                    }
                }
            }
            for(const auto & str:tset)
                list.erase(str);
            if(!que.empty())
                que.push("");
        }
        if(flag) return 0;
        return depth;
    }
};

```

**Complexity Analytics**

- Time Complexity: $$O(?)$$
- Space Complexity: $$O(?)$$
