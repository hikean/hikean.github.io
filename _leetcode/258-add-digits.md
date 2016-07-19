---
layout: leetcode
date: 2016-07-16
title: Add Digits
tags: [Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a non-negative integer `num`, repeatedly add all its digits until the result has only one digit.

For example:

Given `num = 38`, the process is like: `3 + 8 = 11`, `1 + 1 = 2`. Since `2` has only one digit, return it.

**Follow up:**

Could you do it without any loop/recursion in O(1) runtime?

**Hint:**

1. A naive implementation of the above process is trivial. Could you come up with other methods? Show More Hint




***

## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
int addDigits(int num) {
    return (num - 1)%9 + 1;
}
```
**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$


**Result:** Accepted **Time:** 8 ms

```c
int addDigits(int num) {
    int ans = 0;
    do
    {
        while(num)
        {
            ans += num%10;
            num /=10;
        }
        num = ans;
        ans  = 0;
    }while(num > 9);
    return num;
}
```

**Complexity Analytics**

- Time Complexity: $$O(log(n))$$
- Space Complexity: $$O(1)$$
