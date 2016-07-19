---
layout: leetcode
date: 2016-07-16
title: Minimum Size Subarray Sum
tags: [Array, Two Pointers, Binary Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array ``[2,3,1,2,4,3]`` and `s = 7`,

the subarray ``[4,3]`` has the minimal length under the problem constraint.


**More practice:**

If you have figured out the $$O(n)$$ solution, try coding another solution of which the time complexity is $$O(n log n)$$.


***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int ret = nums.size();
        for(int i = 1; i < nums.size(); i++)
            nums[i] += nums[i-1];
        if(!nums.size() || nums[nums.size() -1] < s)
            return 0;
        for(int i = 0; i < nums.size(); i++)
        {
            if(nums.back() - (i?nums[i-1]:0) < s) break;
            auto t = lower_bound(nums.begin() + i,nums.end(),s + (i?nums[i-1]:0));
            if(t != nums.end())
                 ret = min(ret,int(t - nums.begin() - i + 1));
        }
        return ret;
    }
};
```
**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(1)$$


## Two Pointers Way

**Result:** Accepted **Time:** 4 ms


```cpp
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        const int sz = nums.size();
        int start = 0, sum = 0, ret = INT_MAX;
        for (int i = 0; i < sz; i++)
        {
            sum += nums[i];
            while (sum >= s)
            {
                ret = min(ret, i - start + 1);
                sum -= nums[start++];
            }
        }
        return ret == INT_MAX ? 0 : ret;
    }
};
```
**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
