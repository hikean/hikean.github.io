---
layout: leetcode
date: 2016-07-16
title: Course Schedule II
tags: [Depth First Search, Graph, Breadth First Search, Topological Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

**For example:**

<pre>
     2, [[1,0]]
</pre>

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

<pre>
     4, [[1,0],[2,0],[3,1],[3,2]]
</pre>

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].


**Note:**

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).


***

## Solution

**Result:** Accepted **Time:** 36 ms

Here should be some explanations.

```cpp
bool cmp(const pair<int,int> & a,const pair<int,int> & b)
{
    return a.second < b.second;
}

class Solution {
public:
    vector<int> findOrder(int num, vector<pair<int, int>>& pre) {
        sort(pre.begin(),pre.end(),cmp);
        vector<int> lim(num+1,-1);
        vector<int> degree(num,0);
        vector<int> ret;
        for(auto x:pre)
            degree[x.first]++;
        for(int i = 1,cnt  = 0; i < pre.size(); i++)
            if(pre[i-1].second!=pre[i].second)
                lim[pre[i-1].second+1] = i;
        if(pre.size())
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
        for(int j = 0; j < num; j++)
        {
            if(que.empty())
                return vector<int>();
            const int t = que.front();que.pop();
            ret.push_back(t);
            for(int i = lim[t]; i < lim[t+1];  i++)
            {
                degree[pre[i].first]--;
                if(!degree[pre[i].first])
                    que.push(pre[i].first);
            }
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
