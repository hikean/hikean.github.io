---
layout: leetcode
date: 2016-06-27
title: Insert Interval
tags: [Array, Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
>
>You may assume that the intervals were initially sorted according to their start times.
>
>**Example 1:**
>
>Given intervals `[1,3],[6,9]`, insert and merge `[2,5]` in as `[1,5],[6,9]`.
>
>**Example 2:**
>
>Given `[1,2],[3,5],[6,7],[8,10],[12,16]`, insert and merge `[4,9]` in as `[1,2],[3,10],[12,16]`.
>
>This is because the new interval `[4,9]` overlaps with `[3,5],[6,7],[8,10]`.
>
>     

***

## Solution

**Result:** Accepted **Time:** 16 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
    auto it = lower_bound(intervals.begin(), intervals.end(), newInterval,
    [](const Interval& a, const Interval &b ){return a.start < b.start;});
    vector<Interval> ret( intervals.begin(),it);
    if(ret.size()&&ret.back().end >= newInterval.start)
        ret.back().end = max(newInterval.end,ret.back().end);
    else
        ret.push_back(newInterval);
    while(it!=intervals.end())
    {
        auto & tmp = ret.back();
        if(tmp.end >= it->start)
            tmp.end = max(tmp.end,it->end);
        else
            ret.push_back(*it);
        ++it;
    }
    return std::move(ret);
}
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
