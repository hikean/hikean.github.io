---
layout: leetcode
date: 2018-03-12
title: Reach a Number
tags: [Mark, ]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

You are standing at position `0` on an infinite number line. There is a goal at position `target`.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

**Example 1:**

```
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
```

**Example 2:**

```
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
```

**Note:**

- `target` will be a non-zero integer in the range `[-10^9, 10^9]`.

***

## Solution

**Result:** Accepted **Time:**   10 ms

Here should be some explanations.

```cpp
class Solution {
public:
    int reachNumber(int target) {
        if(target < 0)
            target = -target;
        int res = sqrt(2*target) - 0.5 + 1e-9, sum;
        for(int i = res; i < res + 4; i ++){
           if(i&1){
               sum = (i+1) /2 * i;
           }else{
               sum = i / 2 * (i + 1);
           }
            int rest = sum - target;
            if(rest >= 0 && (rest % 2) == 0)
                return i;
        }
        return int(res);
    }
};

```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
