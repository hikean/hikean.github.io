---
layout: leetcode
date: 2016-07-17
title: Find Median from Data Stream
tags: [Heap, Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
``[2,3,4]`` , the median is `3`

``[2,3]``, the median is `(2 + 3) / 2 = 2.5`

Design a data structure that supports the following two operations:

- void addNum(int num) - Add a integer number from the data stream to the data structure.
- double findMedian() - Return the median of all elements so far.

**For example:**

<pre>
add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
</pre>



***

## Solution

**Result:** Accepted **Time:**  180 ms

Here should be some explanations.

```cpp
class MedianFinder {
public:
    priority_queue<int,vector<int>,less<int>> low;
    priority_queue<int,vector<int>,greater<int>> up;
    // Adds a number into the data structure.
    void addNum(int num) {
        if(!low.size() || low.top() >= num)
            low.push(num);
        else
            up.push(num);
    }
    void balance()
    {
            while(low.size() > up.size())
                up.push(low.top()),low.pop();
            while(up.size() > low.size())
                low.push(up.top()),up.pop();
    }
    // Returns the median of current data stream
    double findMedian() {
        balance();
        if(low.size() == up.size())
            return 0.5*(low.top()+up.top());
        else if(low.size() > up.size())
            return low.top();
        return up.top();
    }
    MedianFinder(){}
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf;
// mf.addNum(1);
// mf.findMedian();
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
