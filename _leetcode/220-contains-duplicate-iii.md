---
layout: leetcode
date: 2016-07-16
title: Contains Duplicate III
tags: [Binary Search Tree]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

     

***

## Solution

**Result:** Accepted **Time:** 20 ms

Here should be some explanations.

```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        const int ncnt = nums.size();
        vector<pair<int,int>> vect(ncnt);
        for(int i = 0 ; i < ncnt; i++)
            vect[i].first = nums[i],vect[i].second=i;
        sort(vect.begin(),vect.end());
        for(int i = 0,j = 0; i < ncnt; j=++i)
            while( ++j < ncnt && vect[j].first - t <= vect[i].first)
                if(abs(vect[i].second-vect[j].second) <= k)
                    return true;
        return false;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(n)$$
