---
layout: leetcode
date: 2016-06-27
title: Merge Intervals
tags: [Array, Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a collection of intervals, merge all overlapping intervals.
>
>For example,
>
>Given `[1,3],[2,6],[8,10],[15,18]`,
>
>return `[1,6],[8,10],[15,18]`.
>


***

## Solution

**Result:** Accepted **Time:** 20 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<Interval> merge(vector<Interval>& data) {
        sort(data.begin(),data.end(),[](const Interval& a,const Interval & b){return a.start < b.start;});
        auto it = data.begin();
        for(const auto &x:data)
            if(it->end >= x.start)
                it->end = max(x.end,it->end);
            else
                *(++it) = x;
        if(it!=data.end())
            data.erase(++it,data.end());
        return data;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(1)$$
