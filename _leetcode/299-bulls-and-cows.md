---
layout: leetcode
date: 2016-07-17
title: Bulls and Cows
tags: [Hash Table]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

You are playing the following [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

**For example:**

<pre>
Secret number:  "1807"
Friend's guess: "7810"
</pre>

**Hint:** `1` bull and `3` cows. (The bull is `8`, the cows are `0`, `1` and `7`.)
Write a function to return a hint according to the secret number and friend's guess, use `A` to indicate the bulls and `B` to indicate the cows. In the above example, your function should return ``"1A3B"``.

Please note that both secret number and friend's guess may contain duplicate digits, for example:

<pre>
Secret number:  "1123"
Friend's guess: "0111"
</pre>

In this case, the 1st `1` in friend's guess is a bull, the 2nd or 3rd `1` is a cow, and your function should return ``"1A1B"``.
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c

int min_value(int a,int b)
{
    return a>b?b:a;
}

char* getHint(char* secret, char* guess) {
    char * ans  = malloc(sizeof(char)* 32);
    int lena = strlen(secret);
    int lenb = strlen(guess);
    int a = -1, b = -1;
    int bull = 0,cow = 0;
    int s[11] = {0};
    int g[11] = {0};
    while(++a < lena && ++b < lenb)
        if(secret[a] == guess[b])
        {
            bull ++;
            s[secret[a] - '0'] --;
            g[secret[a] - '0'] --;
        }

    while(lena--)
        s[secret[lena] - '0']++;
    while(lenb--)
        g[guess[lenb] - '0']++;
    a = 10;
    while(a--)
        cow += min_value(s[a],g[a]);
    sprintf(ans,"%dA%dB",bull,cow);
    return ans;
}
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
