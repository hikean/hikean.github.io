---
layout: leetcode
date: 2016-07-18
title: Odd Even Linked List 
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

**Example:**

Given `1->2->3->4->5->NULL`,

return `1->3->5->2->4->NULL`.

**Note:**

The relative order inside both the even and odd groups should remain as it was in the input. 

The first node is considered odd, the second node even and so on ...





***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    struct ListNode Odd,Even,*OLast,*ELast;
    OLast = &Odd;
    ELast = &Even;
    Odd.next = NULL;
    Even.next = NULL;
    int i = 1;
    while(head)
    {
        if(i&1)
        {
            OLast->next = head;
            OLast = head;
        }
        else
        {
            ELast->next = head;
            ELast = head;
        }
        i ^=1;
        head = head->next;
    }
    OLast->next = Even.next;
    ELast->next = NULL;
    return Odd.next;
    
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
