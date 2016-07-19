---
layout: leetcode
date: 2016-06-28
title: Clone Graph
tags: [Graph, Depth First Search, Breadth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Question Description
>Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
>
>
>OJ's undirected graph serialization:
>Nodes are labeled uniquely.
>
>We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
>
>As an example, consider the serialized graph <code><font color="red">{<font color="black">0</font>,1,2#</font><font color="blue"><font color="black">1</font>,2#</font><font color="green"><font color="black">2</font>,2}</font></code>.
>
>The graph has a total of three nodes, and therefore contains three parts as separated by #.
>
>  1. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
>  2. Second node is labeled as 1. Connect node 1 to node 2.
>  3. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
>
> Visually, the graph looks like the following:
>
>            1
>           / \
>          /   \
>         0 --- 2
>              / \
>              \_/     
>     

***

## Solution

**Result:** Accepted **Time:** 78 ms

Here should be some explanations.

```cpp
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        unordered_map<int,UndirectedGraphNode *> mp;
        queue<UndirectedGraphNode *> que;
        UndirectedGraphNode * root = NULL;
        if(node)
        {
            root = new UndirectedGraphNode(node->label);
            que.push(node); que.push(root);
            mp[root->label] = root;
        }
        while(!que.empty())
        {
            UndirectedGraphNode * old_node = que.front();que.pop();
            UndirectedGraphNode * new_node = que.front();que.pop();
            for(const auto & x:old_node->neighbors)
                if(mp.count(x->label))
                    new_node->neighbors.push_back(mp[x->label]);
                else
                {
                    UndirectedGraphNode * tmp = new UndirectedGraphNode(x->label);
                    new_node->neighbors.push_back(tmp);
                    mp[x->label] = tmp;
                    que.push(x);que.push(tmp);
                }
        }
        return root;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
