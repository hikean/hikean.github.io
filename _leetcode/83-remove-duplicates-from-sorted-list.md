---
layout: leetcode
date: 2018-06-28
title: Remove Duplicates from Sorted List
tags: [Linked List]
---

* Contents
{:toc #toc_of_keans_blog}


## Question

Given a sorted linked list, delete all duplicates such that each element appear only once.

### Example 1:

```
Input: 1->1->2
Output: 1->2
```
### Example 2:

```
Input: 1->1->2->3->3
Output: 1->2->3
```



## Solution

**Result:** Accepted **Time:** 4 ms

Here should be some explanations.

```c
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode  Head,*last,*now;
    if(head == NULL)
        return head;
    Head.next = head;
    last = & Head;
    now = head;
    Head.val = now->val + 1;

    while(now)
    {
        if(last->val == now->val)
        {
            last->next = now->next;
            free(now);
            now = last->next;
        }
        else
        {
            last=now;
            now=now->next;
        }
    }
    return Head.next;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
