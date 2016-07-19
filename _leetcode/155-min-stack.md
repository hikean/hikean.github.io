---
layout: leetcode
date: 2016-07-15
title: Min Stack
tags: [Stack, Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
>
>  - push(x) -- Push element x onto stack.
>  - pop() -- Removes the element on top of the stack.
>  - top() -- Get the top element.
>  - getMin() -- Retrieve the minimum element in the stack.
>
> **Example:**
>
>     MinStack minStack = new MinStack();
>     minStack.push(-2);
>     minStack.push(0);
>     minStack.push(-3);
>     minStack.getMin();   --> Returns -3.
>     minStack.pop();
>     minStack.top();      --> Returns 0.
>     minStack.getMin();   --> Returns -2.
>
>     

***

## Solution

**Result:** Accepted **Time:** 28 ms

Here should be some explanations.

```cpp
class MinStack {
    stack<int> sta;
    stack<int> min_sta;
public:
    void push(int x) {
        sta.push(x);
        if(min_sta.empty())
        {
            min_sta.push(x);
            return;
        }
        min_sta.push(min(min_sta.top(),x));
    }

    void pop() {
        sta.pop();
        min_sta.pop();
    }

    int top() {
        return sta.top();
    }

    int getMin() {
        return min_sta.top();
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
