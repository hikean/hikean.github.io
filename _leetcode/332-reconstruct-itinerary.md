---
layout: leetcode
date: 2016-07-18
title: Reconstruct Itinerary
tags: [Graph, Depth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a list of airline tickets represented by pairs of departure and arrival airports `[from, to]`, reconstruct the itinerary in order. All of the tickets belong to a man who departs from `JFK`. Thus, the itinerary must begin with `JFK`.

**Note:**

1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
2. All airports are represented by three capital letters (IATA code).
3. You may assume all tickets form at least one valid itinerary.

**Example 1:**

`tickets` = `[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]`

Return `["JFK", "MUC", "LHR", "SFO", "SJC"]`.

**Example 2:**

`tickets` = `[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]`

Return `["JFK","ATL","JFK","SFO","ATL","SFO"]`.

Another possible reconstruction is `["JFK","SFO","ATL","JFK","ATL","SFO"]`. But it is larger in lexical order.





***

## Solution

**Result:** Accepted **Time:**  32 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        unordered_map<string, multiset<string>> graph;
        for(const auto & x:tickets)
            graph[x.first].insert(x.second);
        vector<string> marching, itinerary;
        marching.push_back("JFK");
        while(marching.size())
        {
            auto from = marching.back();
            if(graph.count(from) && graph[from].size()>0)
            {
                auto & to = graph[from];
                marching.push_back(*to.begin());
                to.erase(to.begin());
            }
            else
            {
                itinerary.push_back(from);
                marching.pop_back();
            }
        }
        reverse(itinerary.begin(), itinerary.end());
        return itinerary;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
