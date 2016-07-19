---
layout: leetcode
date: 2016-05-27
title: Two Sum
tags: [Array, Hash Table]
---

* Contents
{:toc #toc_of_keans_blog}

**本博客主要基于LeetCode[官方题解](https://leetcode.com/articles/two-sum/)**

## Question

>Given an array of integers, return indices of the two numbers such that they add up to a specific target.
>You may assume that each input would have exactly one solution.
>
> ### Example:
>
>     Given nums = [2, 7, 11, 15], target = 9,
>     Because nums[0] + nums[1] = 2 + 7 = 9,
>     return [0, 1].
>
>  **UPDATE (2016/2/13):**<br/>
> The return format had been changed to zero-based indices. Please read the above updated description carefully.




***

## Brute Force Way

**Result:** Accepted   **Time:** 668ms

This way is very simple，Loop through each element $$x$$ and find if there is another value that equals to $$target−x$$.

**Solution in CPP:**

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const int len = nums.size();
        for(int i = 0; i < len; i++)
            for(int j = i + 1; j < len; j++)
                if(nums[i] + nums[j] == target)
                    return vector<int>(i,j);
        return vector<int>();
    }
};
```

**Complexity Analysis**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(1)$$

## Binary Search Way

**Result:** Accepted **Time:** 12ms

In this way, we use a struct to record the value and its index, and sort the vector. Then we loop through each value $$x$$ and use binary search to find if there is another value that equals to $$target-x$$.

```cpp
class Solution {
    struct node{
        int n,pos;
        bool operator < (const node & rhs) const
        { return this->n < rhs.n;}
        node(int v=0,int idx=0):n(v),pos(idx){}
    };
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<node> tmp(nums.size());
        for(int i=0;i<nums.size();i++)
            tmp[i] = node(nums[i],i);
        sort(tmp.begin(),tmp.end());
        for(auto now = tmp.begin();now != tmp.end(); ++now)
        {
            auto it= lower_bound(tmp.begin(),tmp.end(),node(target - now->n));
            if(now != it && it != tmp.end() && it->n == target - now->n)
                return vector<int>{now->pos,it->pos};
        }
        return vector<int>();
    }
};
```
**Complexity Analysis**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(n)$$

## Two Pointers Way
**Result:**  Accepted  **Time:** 12ms

```cpp
class Solution {
    struct Node{
        int n,pos;
        Node(int v=0,int idx=0):n(v),pos(idx){}
        bool operator < (const Node & rhs) const
        {   return this->n < rhs.n;}
    };
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<Node> tmp(nums.size());
        for(int i=0;i<nums.size();i++)
            tmp[i] = Node(nums[i],i);
        sort(tmp.begin(),tmp.end());
        int left = 0, right = nums.size() - 1;
        while(left < right)
        {
            int sum = tmp[left].n + tmp[right].n;
            if(sum > target)
                right --;
            else if(sum == target)
                return vector<int>{tmp[left].pos,tmp[right].pos};
            else left ++;
        }
        return vector<int>();
    }
};
```

**Complexity Analysis**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(n)$$

## Two-Pass Hash Table

**Result:** Accepted **Time:** 20ms

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;
        int index = 0;
        for(const auto & x:nums)
            mp[x] = index++;
        index = 0;
        for(const auto & x:nums)
            if(++index && mp.count(target-x) && mp[target-x]!=index-1)
                return vector<int>{index-1,mp[target-x]};
        return vector<int>();
    }
};
```
**Complexity Analysis**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$

## One Pass Hash Table
**Result:** Accepted **Time:** 20ms

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;
        int index = 0;
        for(const auto & x:nums){
            if(mp.count(target-x))
                return vector<int>{index,mp[target-x]};
            mp[x] = index++;
        }
        return vector<int>();
    }
};
```

**Complexity Analysis**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
