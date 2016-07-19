---
layout: leetcode
date: 2016-07-17
title: Nim Game
tags: [Brainteaser]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

**Hint:**

1. If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?


***

## Solution

**Result:** Accepted **Time:**  0 ms

Here should be some explanations.

```c
bool canWinNim(int n) {
    return n&3;
}
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
