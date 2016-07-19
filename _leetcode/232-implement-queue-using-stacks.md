---
layout: leetcode
date: 2016-07-16
title: Implement Queue using Stacks
tags: [Stack, Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Implement the following operations of a queue using stacks.

- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

**Notes:**

- You must use only standard operations of a stack -- which means only `push to top`, p`eek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
- You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).





***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```cpp
#include<stack>
using std::stack;

class Queue {
    void reset()
    {
        if(stack_out.empty())
        {
            while(!stack_in.empty())
            {
                stack_out.push(stack_in.top());
                stack_in.pop();
            }
        }
    }
    stack<int> stack_in;
    stack<int> stack_out;
public:
    // Push element x to the back of queue.

    void push(int x) {
        stack_in.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
        this->reset();
        stack_out.pop();
    }

    // Get the front element.
    int peek(void) {
        this->reset();
        return stack_out.top();
    }

    // Return whether the queue is empty.
    bool empty(void) {
        this->reset();
        return stack_out.empty();
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
