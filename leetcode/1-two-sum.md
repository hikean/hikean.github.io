---
layout: post
date: 2016-05-27
title: Two Sum
tags: [leetcode,algorithm]
---


```cpp
class Solution {
    struct node{
        int n,pos;
        bool operator < (const node & rhs) const
        {
            return this->n < rhs.n;
        }
    };
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        vector<node> tmp(nums.size());
        bool ok=false;
        for(int i=0;i<nums.size();i++)
        {
            tmp[i].n=nums[i];
            tmp[i].pos=i+1;
        }
        sort(tmp.begin(),tmp.end());
        for(vector<node>::iterator now = tmp.begin();now != tmp.end(); ++now)
        {
            node des;
            des.n=target - now->n;
            vector<node>::iterator it= lower_bound(tmp.begin(),tmp.end(),des);
            if(now != it && it != tmp.end() && it->n == target - now->n)
            {
                ans.push_back(now->pos);
                ans.push_back(it->pos);
                if(ans[0] > ans[1])
                    swap(ans[0],ans[1]);
                return ans;
            }
        }
        return ans;
    }
};

```
