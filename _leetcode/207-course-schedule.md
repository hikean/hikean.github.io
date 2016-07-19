---
layout: leetcode
date: 2016-07-16
title: Course Schedule
tags: [Depth First Search, Graph, Breadth First Search, Topological Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 There are a total of n courses you have to take, labeled from `0` to `n - 1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: ``[0,1]``

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

**For example:**

<pre>
     2, [[1,0]]
</pre>

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

<pre>
     2, [[1,0],[0,1]]
</pre>

There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

**Note:**

 The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
     

***

## Solution

**Result:** Accepted **Time:** 24 ms

Here should be some explanations.

```cpp
bool cmp(const pair<int,int> & a,const pair<int,int> & b)
{
    return a.second < b.second;
}

class Solution {
public:
    bool canFinish(int num, vector<pair<int, int>>& pre) {
        if(!pre.size())
            return true;
        sort(pre.begin(),pre.end(),cmp);
        vector<int> lim(num+1,-1);
        vector<int> degree(num,0);
        for(auto x:pre)
            degree[x.first]++;
        for(int i = 1,cnt  = 0; i < pre.size(); i++)
            if(pre[i-1].second!=pre[i].second)
                lim[pre[i-1].second+1] = i;
        lim[pre.back().second+1] = pre.size();
        for(int i = 0,llast = 0; i <= num; i++)
            if(lim[i] < 0)
                lim[i] = llast;
            else
                llast = lim[i];
        queue<int> que;
        for(int i = 0; i < num; i++)
            if(!degree[i])
                que.push(i);
        while(!que.empty())
        {
            const int t = que.front();que.pop();
            for(int i = lim[t]; i < lim[t+1];  i++)
            {
                degree[pre[i].first]--;
                if(!degree[pre[i].first])
                    que.push(pre[i].first);
            }
        }
        for(auto x:degree)
            if(x)
                return false;
        return true;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
