---
layout: leetcode
date: 2016-07-15
title: Insertion Sort List
tags: [Linked List, Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>
> Sort a linked list using insertion sort.
>     

***

## Solution

**Result:** Accepted **Time:** 80 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode * insert(struct ListNode * head,struct ListNode *node)
{
    if(head == NULL)
    {
        node->next = NULL;
        return node;
    }
    struct ListNode Head,*last;
    Head.next = head;
    last = &Head;
    int value = node->val;
    while(last->next!=NULL && value > last->next->val )
        last = last->next;
    node->next = last->next;
    last->next = node;
    return Head.next;
}
struct ListNode* insertionSortList(struct ListNode* head) {
    struct ListNode Head, *tmp;
    Head.next = NULL;
    while(head)
     {
         tmp = head->next;
         Head.next = insert(Head.next,head);
         head = tmp;
     }
     return Head.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
