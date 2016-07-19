---
layout: leetcode
date: 2016-07-15
title: Sort List
tags: [Linked List, Sort]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>
> Sort a linked list in $$ O(n log n)$$ time using constant space complexity.
>

***

## Solution

**Result:** Accepted **Time:** 16 ms

Here should be some explanations.

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode * get_tail(struct ListNode * head)
{
    while(head!=NULL && head->next!=NULL)
        head = head->next;
    return head;
}
#define INC_ORDER 1
#define DEC_ORDER 2
#define NO_ORDER 0
int is_sorted(struct ListNode * head)
{
    int last = head->val;
    head = head -> next;
    int ans = 3,tmp;
    while(head&&ans)
    {
        tmp = head->val;
        if(last > tmp) // DEC not INC
            ans &= DEC_ORDER;
        if(last < tmp) // INC not DEC
            ans &= INC_ORDER;
        last = tmp;
        head = head->next;
    }
    return ans;
}

struct ListNode * reverse(struct ListNode* head)
{
    struct ListNode Head, *tmp;
    Head.next = NULL;
    while(head)
    {
        tmp = head;
        head = head->next;
        tmp->next = Head.next;
        Head.next = tmp;
    }
    return Head.next;
}
struct ListNode *linksort(struct ListNode* head)
{

    if(head == NULL || head->next == NULL) return head;
    int ord = is_sorted(head);
    if(ord == INC_ORDER) return head;
    else if(ord == DEC_ORDER)
        return reverse(head);
    struct ListNode low, up,mid;
    struct ListNode * llast = &low, *ulast = &up,*mlast=head;
    struct ListNode **tmp = NULL;
    bool inc = true,dec = true;
    mid.next = head;
    head = head->next;
    int value = mlast->val;
    while(head!=NULL)
    {
        tmp = head->val < value ? (&llast):(&ulast);
        if(head->val == value)
            tmp = &mlast;
        (*tmp)->next = head;
        (*tmp) = head;
        head = head->next;
    }
    llast->next = NULL;
    ulast->next = NULL;
    low.next = linksort(low.next);
    up.next = linksort(up.next);
    mlast->next = up.next;
    if(low.next)
    {
        get_tail(low.next)->next = mid.next;
        return low.next;
    }
    return mid.next;
}
struct ListNode* sortList(struct ListNode* head) {
    return linksort(head);
}


```

**Complexity Analytics**

- Time Complexity: $$O(n*log(n))$$
- Space Complexity: $$O(log(n))$$
