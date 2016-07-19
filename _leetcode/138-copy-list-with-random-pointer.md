---
layout: leetcode
date: 2016-07-13
title: Copy List with Random Pointer
tags: [Hash Table, Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
>
>Return a deep copy of the list.
>
>     

***

## Solution

**Result:** Accepted **Time:** 224 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     struct RandomListNode *next;
 *     struct RandomListNode *random;
 * };
 */

struct RandomListNode * get_random_node(struct RandomListNode *origin,struct RandomListNode * newly,struct RandomListNode *ptr)
{
    while(origin && origin != ptr)
    {
        origin = origin -> next;
        newly = newly -> next;
    }
    return newly;
}
struct RandomListNode *copyRandomList(struct RandomListNode *head) {
    struct RandomListNode Head, *last,*origin = head;
    if(head == NULL)
        return NULL;
    Head.next = NULL;
    last = &Head;
    while(head)
    {
        last->next = malloc(sizeof(struct RandomListNode));
        last = last->next;
        last -> label = head -> label;
        head = head -> next;
    }
    last->next = NULL;
    last = Head.next;
    head = origin;
    while(last)
    {
        if(head->random == NULL)
            last->random = NULL;
        else
            last->random = get_random_node(origin,Head.next,head->random);
        last = last->next;
        head = head->next;
    }
    return Head.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(1)$$
