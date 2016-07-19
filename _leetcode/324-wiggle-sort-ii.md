---
layout: leetcode
date: 2016-07-18
title: Wiggle Sort II
tags: [Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an unsorted array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`.

**Example:**

1. Given nums = `[1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`. 
2. Given nums = `[1, 3, 2, 2, 3, 1]`, one possible answer is `[2, 3, 1, 3, 1, 2]`.

**Note:**

You may assume all input has valid answer.

**Follow Up:**

Can you do it in O(n) time and/or in-place with O(1) extra space?



***

## Solution

**Result:** Accepted **Time:**  77 ms

Here should be some explanations.

```cpp
/*class Solution {
public:
   // void wiggleSort(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i = (nums.size()-1)/2,j=(nums.size()+1)/2; j < nums.size(); i-=2,j+=2)
            swap(nums[i],nums[j]);
    }
};*/

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        vector<int> temp(nums);
        std:sort(temp.begin(), temp.end()); //sort the array in the ascending order
        int i, len=nums.size(), k = (len+1)/2, j=len;
        for(i=0; i<len; ++i)
            nums[i] = i & 1? temp[--j]:temp[--k]; // interleave the small half and large half in a reverse order (i.e. --j, --k)
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(n)$$
