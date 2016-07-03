---
layout: leetcode
date: 2016-06-17
title: Add Two Numbers
tags: [Linked List, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
>
>     Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
>     Output: 7 -> 0 -> 8

***

## Solution

**Result:** Accepted **Time:** 20ms

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode  head(0);
        ListNode * tail = &head;
        int carry = 0;
        while(l1 || l2 )
        {
            if(l1)
                carry += l1 -> val, l1 = l1->next;
            if(l2)
                carry += l2 -> val, l2 = l2->next;
            tail->next =  new ListNode(carry%10);
            tail = tail->next;
            carry /= 10;
        }
        if(carry)
            tail->next = new ListNode(carry);
        return head.next;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(max(m,n))$$
- Space Complexity: $$O(max(m,n))$$
