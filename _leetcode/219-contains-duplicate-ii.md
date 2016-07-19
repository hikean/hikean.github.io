---
layout: leetcode
date: 2016-07-16
title: Contains Duplicate II
tags: [Array, Hash Table]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that **nums[i] = nums[j]** and the difference between i and j is at most k.

     

***

## Solution

**Result:** Accepted **Time:** 20 ms

Here should be some explanations.

```cpp
struct Node{
    int n,idx;
    bool operator < (const Node & rhs) const
    {
        return this->n < rhs.n;
    }
    Node():n(0),idx(0){}
    Node(int _n,int _i):n(_n),idx(_i){}
};

inline int int_abs(int arg)
{
    return arg > 0? arg : -arg;
}

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        const int nums_cnt = nums.size();
        if(nums_cnt == 0)
            return false;
        if(k < 50 || nums_cnt < 1024)
            for(int i = 0; i < nums_cnt; i++)
            {
                for(int j = i + 1 ; j < i + k && j < nums_cnt; j++)
                    if(nums[i] == nums[j])
                        return true;
            }
        //return false;
        vector<Node> * vect = new vector<Node>(nums_cnt);
        for(int i = 0; i < nums_cnt; i++)
            (*vect)[i] = Node(nums[i],i);
        sort((*vect).begin(),(*vect).end());
        int strt = 0;
        int tar = (*vect)[strt].n;
        int ii,jj,dst;
        while(true)
        {
            if( strt >= nums_cnt)
                break;
            tar = (*vect)[strt].n;
            dst = strt-1;
            while((*vect)[++dst].n == tar);
            if(dst - strt > 1)
            {
                for(ii = strt; ii < dst; ii++)
                    for(jj = ii + 1; jj < dst; jj++)
                        if(int_abs((*vect)[ii].idx -(*vect)[jj].idx) <= k)
                            return true;

            }
            strt = dst;
        }
        delete vect;
        return false;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
