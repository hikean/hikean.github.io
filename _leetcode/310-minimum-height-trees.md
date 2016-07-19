---
layout: leetcode
date: 2016-07-17
title: Minimum Height Trees
tags: [Breadth First Search, Graph]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

**Format**

The graph contains n nodes which are labeled from `0` to `n - 1`. You will be given the number `n` and a list of undirected `edges` (each edge is a pair of labels).

You can assume that no duplicate edges will appear in `edges`. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in `edges`.

**Example 1:**

Given `n = 4`, `edges = [[1, 0], [1, 2], [1, 3]]`

<pre>

        0
        |
        1
       / \
      2   3

</pre>

return `[1]`

**Example 2:**

Given `n = 6`, `edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]`

<pre>
     0  1  2
      \ | /
        3
        |
        4
        |
        5
 </pre>
        
return `[3, 4]`

**Hint:**

1. How many MHTs can a graph have at most?

**Note:**

- According to the [definition of tree on Wikipedia](https://en.wikipedia.org/wiki/Tree_(graph_theory)): “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

- The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.




***

## Solution

**Result:** Accepted **Time:**  84 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
                vector<vector<int> > adj_list(n);
                vector<int> counters(n, 0),res;
                for (const auto &e : edges) {
                    adj_list[e.first].push_back(e.second);
                    adj_list[e.second].push_back(e.first);
                    ++counters[e.first];++counters[e.second];
                }
                queue<int> q;
                for (int i = 0; i < n; ++i)
                    if (counters[i] <= 1)
                        q.push(i);
                while (n > 2) {
                    const int num_leafs = q.size();
                    n -= num_leafs;
                    for (int i = 0; i < num_leafs; ++i) {
                        int node = q.front();q.pop();
                        for (const auto & neighbor : adj_list[node])
                            if (--counters[neighbor] == 1)
                                q.push(neighbor);
                    }
                }
                while (!q.empty()) res.push_back(q.front()),q.pop();
                return res;
            }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
