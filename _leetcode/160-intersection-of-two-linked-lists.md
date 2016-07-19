---
layout: leetcode
date: 2016-07-15
title: Intersection of Two Linked Lists
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

<pre>
     A:          a1 → a2
                        ↘
                          c1 → c2 → c3
                        ↗            
     B:     b1 → b2 → b3
</pre>     

 begin to intersect at node c1.

**Notes:**


  - If the two linked lists have no intersection at all, return `null`.
  - The linked lists must retain their original structure after the function returns.
  - You may assume there are no cycles anywhere in the entire linked structure.
  - Your code should preferably run in O(n) time and use only O(1) memory.


***

## Solution

**Result:** Accepted **Time:** 36 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode * a = headA,*b = headB,*tmp;
    int cnt = 0;
    while(a && b)
    {
        a = a->next;
        b = b->next;
        cnt ++;
    }
    if(a == NULL)
    {
        tmp = headB;
        while(b)
            tmp = tmp->next,
            b = b->next;
        b = tmp;
        a = headA;
    }
    if(b == NULL)
    {
        tmp = headA;
        while(a)
            a = a->next,
            tmp = tmp->next;
        a = tmp;
        b = headB;
    }
    while(a != b && a && b)
    {
        a = a->next;
        b = b->next;
    }
    if(a && b) return a;
    return NULL;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
