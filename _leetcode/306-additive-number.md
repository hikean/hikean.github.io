---
layout: leetcode
date: 2016-07-17
title: Additive Number
tags: [Depth First Search, Math, String, Dynamic Programming]
---

* Contents
{:toc #toc_of_keans_blog}

## Question


Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain **at least** three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:

`"112358"` is an additive number because the digits can form an additive sequence: `1, 1, 2, 3, 5, 8`.

<pre>
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

`"199100199"` is also an additive number, the additive sequence is: `1, 99, 100, 199`.

<pre>
1 + 99 = 100, 99 + 100 = 199
</pre>

**Note:** Numbers in the additive sequence **cannot** have leading zeros, so sequence `1, 2, 03` or `1, 02, 3` is invalid.

Given a string containing only digits `'0'-'9'`, write a function to determine if it's an additive number.

**Follow up:**

How would you handle overflow for very large input integers?




***

## Solution

**Result:** Accepted **Time:**  0 ms

Here should be some explanations.

```c
bool plus_equal(char * num, int i, int j, int k)
{
    int carry = 0, a = i, b = j, c = k;
    if((num[0] == '0'&& i > 1)  || (num[i]== '0' && j  > i+1) || (num[j] == '0'&& k > j+1))
        return false;
    while(a > 0 || b > i || carry)
    {
        if(c <= j) return false;
        if(a > 0)
            carry += num[--a] - '0';
        if(b > i)
            carry += num[--b] - '0';
        if(carry%10 != num[--c] - '0')
            return false;
        carry /= 10;
    }
    return c == j;
}
bool dfs(char *num,int i,int j,int len)
{
    if(j >= len)
        return true;
    int k = i+j;
    if(k < j*2 - i)
        k = j*2 - i;
    if(k <=len && plus_equal(num,i,j,k) && dfs(num+i,j-i,k-i,len - i))
        return true;
    if(k < len && plus_equal(num,i,j,k+1) && dfs(num+i,j-i,k+1-i,len - i))
        return true;
    return false;
}

bool isAdditiveNumber(char* num){
    const int len  = strlen(num);
    for(int i = 1; i <= len/2; i++)
        for(int j = i+1 ; j < len; j++)
            if(dfs(num,i,j,len))
                return true;
    return false;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(1)$$
