---
layout: leetcode
date: 2016-06-26
title: Reverse Nodes in k-Group
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
>If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
>
>You may not alter the values in the nodes, only nodes itself may be changed.
>
>Only constant memory is allowed.
>
>For example,
>
> Given this linked list: `1->2->3->4->5`
>
> For $$k = 2$$, you should return: `2->1->4->3->5`
>
> For $$k = 3$$, you should return: `3->2->1->4->5`
>     

***

## Solution

**Result:** Accepted **Time:** 8ms

Here should be some explanations.

```c
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode Head;
    register struct ListNode *now = &Head,*last = &Head,*tmp;
    int cnt = 0;
    Head.next = NULL;
    while(head)
    for(cnt = 0,now = last,last = head; cnt < k &&head; cnt++)
    {
        tmp = head;
        head = head->next;
        tmp -> next = now -> next;
        now->next = tmp;
    }
    if(k != cnt)
    for(head = now->next,now -> next = NULL;head;)
    {
        tmp = head;
        head = head->next;
        tmp -> next = now -> next;
        now->next = tmp;
    }
    return Head.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
