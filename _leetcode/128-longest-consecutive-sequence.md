---
layout: leetcode
date: 2016-07-13
title: Longest Consecutive Sequence
tags: [Array, Union Find]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
>
>For example,
>
>Given `[100, 4, 200, 1, 3, 2]`,
>
>The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its length: `4`.
>
> Your algorithm should run in $$O(n)$$ complexity.
>


***

## Solution

**Result:** Accepted **Time:** 24 ms

Here should be some explanations.

## Hash Table Way

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> mp;
        int ret = 0;
        for(const auto x:nums)
            //if(mp.count())
            mp.insert(x);
        while(mp.size())
            {
                int x = *mp.begin();
                int left = x,right = x+1;
                while(mp.count(left))
                    mp.erase(left--);
                while(mp.count(right))
                    mp.erase(right++);
                ret = max(ret,right - left  - 1);
            }
        return ret;
    }
};
```

## Union Find Way

```cpp
class Solution {
    vector<int> id;
    vector<int> size;
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if(n < 2) return n;
        size = vector<int>(n,1);
        for(int i = 0; i < n; i++) {
            id.push_back(i);
        }
        unordered_map<int,int> record;
        for(int i = 0 ; i < n; i++) {
            if(record.find(nums[i]) != record.end()) continue;
            record[nums[i]] = i;
            if(record.find(nums[i]-1) != record.end()) {
                unionSet(i,record[nums[i]-1]);
            }
            if(record.find(nums[i]+1) != record.end()) {
                unionSet(i,record[nums[i]+1]);
            }
        }
        int res = *max_element(size.begin(),size.end());
        return res;
    }

    int find(int p) {
        while(p != id[p]) {
            id[p] = id[id[p]];
            p = id[p];
        }
        return p;
    }
    void unionSet(int a, int b) {
        int i = find(a);
        int j = find(b);
        if(i == j) return;
        if(size[i] > size[j]) {
            id[j] = i;
            size[i] += size[j];
        } else {
            id[i] = j;
            size[j] += size[i];
        }
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
