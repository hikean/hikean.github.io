---
layout: leetcode
date: 2016-07-18
title: Top K Frequent Elements
tags: [Hash Table, Heap]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a non-empty array of integers, return the <i><b>k</b><i> most frequent elements.

For example,

Given `[1,1,1,2,2,3]` and k = `2`, return `[1,2]`.

**Note:**

- You may assume <i><b>k</b><i> is always valid, 1 ≤ <i><b>k</b><i> ≤ number of unique elements.
- Your algorithm's time complexity **must be** better than *O(n log n)*, where *n* is the array's size.



***

## Solution

**Result:** Accepted **Time:**  36 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        vector<int> ret(k);
        int max_frequence = 0,last,cnt = 0;
        for(auto x:nums)
            max_frequence = max(++mp[x],max_frequence);
        vector<int> frequence(max_frequence + 1);
        for(auto x:mp)
            frequence[x.second]++;
        for(int i = max_frequence; k > 0; i--)
            k -= frequence[last=i];
        for(auto x:mp)
        {
            if(x.second >= last)
                ret[cnt++] = x.first;
            else if(cnt >= nums.size()) 
                break;
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
