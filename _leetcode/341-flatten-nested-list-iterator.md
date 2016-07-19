---
layout: leetcode
date: 2016-07-18
title: Flatten Nested List Iterator
tags: [Stack, Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

**Example 1:**

Given the list `[[1,1],2,[1,1]]`,

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: `[1,1,2,1,1]`.

**Example 2:**

Given the list `[1,[4,[6]]]`,

By calling *next repeatedly* until *hasNext* returns false, the order of elements returned by *next* should be: `[1,4,6]`.



***

## Solution

**Result:** Accepted **Time:**  32 ms

Here should be some explanations.

```cpp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
private:
    queue<int> q;
    void inqueue(vector<NestedInteger> &nestedList)
    {
        for(int i = 0; i < nestedList.size(); i++)
        {
            if(nestedList[i].isInteger())
            {
                q.push(nestedList[i].getInteger());
            }
            else
            {
                inqueue(nestedList[i].getList());
            }
        }
    }
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        inqueue(nestedList);
    }

    int next() {
        int x = q.front();
        q.pop();
        return x;
    }

    bool hasNext() {
        return !q.empty();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
