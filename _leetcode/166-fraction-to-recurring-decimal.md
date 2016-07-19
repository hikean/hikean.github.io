---
layout: leetcode
date: 2016-07-15
title: Fraction to Recurring Decimal
tags: [Hash Table, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

  - Given numerator = 1, denominator = 2, return "0.5".
  - Given numerator = 2, denominator = 1, return "2".
  - Given numerator = 2, denominator = 3, return "0.(6)".


***

## Solution

**Result:** Accepted **Time:** 0 ms

Here should be some explanations.

```c
#define MAXN 4096
char buff[MAXN];
long long rest[MAXN], result[MAXN];

char *fractionToDecimal(int num, int den)
{
    long long d = den;
    int md = 0, cnt = -1, ptr = 0;
    long long n = num;
    if(n < 0) n = -n;
    if(d < 0) d = -d;
    bool dot = n%d;
    bool flag = true;
    result[0] = 0;
    while(flag && n)
    {
        result[++cnt] = n / d;
        n %= d;
        for(int i = 1; i < 10 && i < cnt && flag; i++)
                flag = !(rest[md=i] == n);
        rest[cnt] = n;
        n *= 10;
    }
    if(result[1] == result[cnt] && cnt != 1) cnt--,md--;
    if((num^den)&INT_MIN && num)
        buff[ptr++] = '-';
    sprintf(buff+ptr, "%lld", result[0]);
    while (buff[ptr]) ptr++;
    if (dot)
        buff[ptr++] = '.';
    for (int i = 1; i <= md; i++)
        buff[ptr++] = '0' + result[i];
    if (n) buff[ptr++] = '(';
    for(int i = md+1; i <= cnt; i++)
        buff[ptr++] = '0' + result[i];
    if (n) buff[ptr++] = ')';
    buff[ptr] = 0;
    return buff;
}

```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(n)$$
