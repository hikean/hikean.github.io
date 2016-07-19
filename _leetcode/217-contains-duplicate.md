---
layout: leetcode
date: 2016-07-16
title: Contains Duplicate
tags: [Array, Hash Table]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
     

***

## Solution

**Result:** Accepted **Time:** 40 ms

Here should be some explanations.

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i=1;i<nums.size();i++)
            if(nums[i]==nums[i-1])
                return true;
        return false;
    }
    bool containsDuplicate2(vector<int>& nums) {
        set<int> st;
        int i=0, j = nums.size() -1,k=0,tmp;
        while(i<=j)
        {
            k^=1;
            if(k)
                tmp = nums[i++];
            else
                tmp = nums[j--];
            if(st.count(tmp)) return true;
            st.insert(tmp);
        }
        return false;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
