---
layout: leetcode
date: 2016-07-16
title: Palindrome Linked List
tags: [Linked List, Two Pointers]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Given a singly linked list, determine if it is a palindrome.

**Follow up:**

Could you do it in $$O(n)$$ time and $$O(1)$$ space?



***

## Solution

**Result:** Accepted **Time:** 12 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode * reverse(struct ListNode * head)
{
    struct ListNode *rhead = NULL,*tmp;
    while(head != NULL)
    {
        tmp = head;
        head = head->next;
        tmp ->next = rhead;
        rhead = tmp;
    }
    return rhead;
}
int get_len(struct ListNode * head)
{
    int len = 0;
    while(head)
    {
        len ++;
        head = head->next;
    }
    return len;
}

struct ListNode * get_nth_node(struct ListNode * head,int n)
{
    while(n-- && head)
        head = head->next;
    return head;
}

bool isPalindrome(struct ListNode* head) {
    struct ListNode * rhead,*t,*p;
    int len = get_len(head);
    bool ans  = true;
    rhead = get_nth_node(head,(len+1)/2);
    rhead = reverse(rhead);
    p = head;
    t = rhead;
    len = len/2;

    while(len--)
    {
        if(p->val != t->val)
        {
            ans = false;
            break;
        }
        p = p->next;
        t = t->next;
    }
    reverse(rhead);
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
