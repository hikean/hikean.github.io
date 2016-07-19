---
layout: leetcode
date: 2016-07-16
title: Implement Stack Using Queues
tags: [Stack, Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Implement the following operations of a stack using queues.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.

**Notes:**

- You must use only standard operations of a queue -- which means only `push to back`, `peek/pop from front`, `size`, and `is empty` operations are valid.
- Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
- You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).



***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
class Stack {
    queue<int> que;
public:
    // Push element x onto stack.
    void push(int x) {
        que.push(x);

    }

    // Removes the element on top of the stack.
    void pop() {
        int n = que.size();
        if(n<1) return ;
        while(--n)
        {
            que.push(que.front());
            que.pop();
        }
        que.pop();
    }

    // Get the top element.
    int top() {
        return que.back();
    }

    // Return whether the stack is empty.
    bool empty() {
        return que.empty();
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
