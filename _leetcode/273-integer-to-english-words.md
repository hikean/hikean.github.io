---
layout: leetcode
date: 2016-07-17
title: Integer to English Words
tags: [ ]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than $$2^{31} - 1$$.

For example,
<pre>
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
</pre>

**Hint:**

1. Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
2. Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
3. There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)



***

## Solution

**Result:** Accepted **Time:**  4 ms

Here should be some explanations.

```c
char ret[512];
const char *ones[]={
    "","enO ","owT ","eerhT ","ruoF ","eviF ","xiS ","neveS ","thgiE ","eniN ","neT ","nevelE ","evlewT ","neetrihT ","neetruoF ","neetfiF ","neetxiS ","neetneveS ","neethgiE ","neeteniN ",};

const char * tens[]={"","neT ","ytnewT ","ytrihT ","ytroF ","ytfiF ","ytxiS ","ytneveS ","ythgiE ","yteniN ",};
const char *thous[]={"","dnasuohT ","noilliM ","noilliB "};
const char *hundred = "derdnuH ";
char zero[] ="Zero";
void reverse_str(char * str,int len)
{
    char tmp,*ptr = str+len -1;
    while(str < ptr)
    {
        tmp = *str;
        *(str++) = *ptr;
        *(ptr--) = tmp;
    }
}
int copy_str(const char * str,char * ret,int index)
{
    const char *ptr = str;
    while(*ptr)
        ret[index++] = *(ptr++);
    return index ;
}
char* numberToWords(int num) {
    if(!num)
        return zero;
    int index = 0;
    for(int i = 0; num; i++)
    {
        if(num%1000)
           index = copy_str(thous[i],ret,index);
        int tmp = num%100;num/=100;
        if(tmp < 20)
            index = copy_str(ones[tmp],ret,index);
        else
        {
            index = copy_str(ones[tmp%10],ret,index);
            index = copy_str(tens[tmp/10],ret,index);
        }
        tmp = num % 10;num /= 10;
        if(tmp)
        {
            index = copy_str(hundred,ret,index);
            index = copy_str(ones[tmp],ret,index);
        }
    }
    ret[--index] = '\0';
    reverse_str(ret,index);
    return ret;
}
```

**Complexity Analytics**

- Time Complexity: $$O(1)$$
- Space Complexity: $$O(1)$$
