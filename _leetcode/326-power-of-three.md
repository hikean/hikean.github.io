---
layout: leetcode
date: 2016-07-18
title: Power of Three
tags: [Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given an integer, write a function to determine if it is a power of three.

**Follow up:**

Could you do it without using any **loop** / **recursion**?



***

## Solution

**Result:** Accepted **Time:**  164 ms

Here should be some explanations.

```cpp
class ThreeSet{
    set<int> st;
public:
    ThreeSet(){
        int i = 1;
        while(i >0)
        {
            st.insert(i);
            i*=3;
        }
    }
    int count(int n)
    {
        return st.count(n);
    }
};

class Solution {
   static ThreeSet st;
    
public:
    
    bool isPowerOfThree(int n) {
        return st.count(n);
    }
};

ThreeSet Solution::st;
```

**Complexity Analytics**

- Time Complexity: $$O(log(log(n)))$$
- Space Complexity: $$O(1)$$
