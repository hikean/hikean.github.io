---
layout: leetcode
date: 2016-07-16
title: Sliding Window Maximum
tags: [ ]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,

Given nums = ``[1,3,-1,-3,5,3,6,7]``, and `k = 3`.

<pre>
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 </pre>

Therefore, return the max sliding window as ``[3,3,5,5,6,7]``.

**Note:**

You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.


**Follow up:**

Could you solve it in linear time?


**Hint:**

1. How about using a data structure such as deque (double-ended queue)?

***

## Solution

**Result:** Accepted **Time:** 116 ms

Here should be some explanations.

```cpp

struct Node{
    int value,index;
    Node():value(0),index(0){}
    Node(int v,int i):value(v),index(i){}
    bool operator < (const Node & rht) const
    {
        return this->value < rht.value;
    }
};
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<Node> que;
        vector<int> ret;
        for(int i = 0; i < k - 1;i++)
            que.push(Node(nums[i],i));
        for(int i = k-1; i < nums.size(); i++)
        {
            que.push(Node(nums[i],i));
            Node tmp = que.top();
            while(i - tmp.index >= k)
            {
                que.pop();
                tmp = que.top();
            }
            ret.push_back(tmp.value);
        }
        return ret;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(nlog(n))$$
- Space Complexity: $$O(1)$$
