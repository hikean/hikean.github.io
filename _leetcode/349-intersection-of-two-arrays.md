---
layout: leetcode
date: 2016-07-18
title: Intersection of Two Arrays
tags: [Binary Search, Hash Table, Two Pointers, Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given two arrays, write a function to compute their intersection.

**Example:**

Given nums1 = `[1, 2, 2, 1]`, nums2 = `[2, 2]`, return `[2]`.

**Note:**

- Each element in the result must be unique.
- The result can be in any order.




***

## Solution

**Result:** Accepted **Time:**  12 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> st(nums1.begin(),nums1.end());
        vector<int> ret;
        for(const auto & x:nums2)
            if(st.count(x))
            {
                ret.push_back(x);
                st.erase(x);
            }
        return std::move(ret);
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
