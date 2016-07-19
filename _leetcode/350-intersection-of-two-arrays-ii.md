---
layout: leetcode
date: 2016-07-18
title: Intersection of Two Arrays II
tags: [Binary Search, Hash Table, Two Pointers, Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given two arrays, write a function to compute their intersection.

**Example:**

Given nums1 = `[1, 2, 2, 1]`, nums2 = `[2, 2]`, return `[2, 2]`.

**Note:**

- Each element in the result should appear as many times as it shows in both arrays.
- The result can be in any order.

**Follow up:**

- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?



***

## Solution

**Result:** Accepted **Time:**  12 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        const int alen = nums1.size(), blen = nums2.size();
        int a = 0, b = 0;
        vector<int> ret;
        while(a < alen && b < blen)
        {
            if( nums1[a] > nums2[b])
                b++;
            else if(nums1[a] < nums2[b])
                a++;
            else
                ret.push_back(nums1[a]),a++,b++;
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(n)$$
