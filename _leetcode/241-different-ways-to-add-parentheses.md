---
layout: leetcode
date: 2016-07-16
title:  Different Ways to Add Parentheses
tags: [Divide and Conquer]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are ``+``, ``-`` and ``*``.


**Example 1**

Input: ``"2-1-1"``.

<pre>
((2-1)-1) = 0
(2-(1-1)) = 2
</pre>

Output: **[0, 2]**


**Example 2**

Input: **"2*3-4*5"**

<pre>
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
</pre>

Output: ``[-34, -14, -10, -10, 10]``




***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```cpp
class Solution {
public:
    vector<int> diffWaysToCompute(const string input) {
        vector<int> result;
        for(int i=0; i< input.size(); i++)
            if(!isdigit(input[i]))
                for(int a : diffWaysToCompute(input.substr(0, i)))
                    for(int b : diffWaysToCompute(input.substr(i+1)))
                        result.push_back(operate(a,b,input[i]));
        return result.size() ? result : vector<int>{stoi(input)};
    }
    inline int operate(int a,int b,char c)
    {
        if(c == '-') return a - b;
        if(c == '+') return a + b;
        return a*b;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(2^n)$$
- Space Complexity: $$O(1)$$
