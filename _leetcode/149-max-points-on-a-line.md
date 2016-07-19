---
layout: leetcode
date: 2016-07-15
title: Max Points on A Line
tags: [Hash Table, Math]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

>
>Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
>     

***

## Solution

**Result:** Accepted **Time:** 28 ms

Here should be some explanations.

```cpp
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
 #define HASH_VALUE (1000000007ll)
class Solution {
public:
    long long gcd(long long a, long long b)
    {
        return !b?a:gcd(b,a%b);
    }
    long long get_rate(const Point & a, const Point & b)
    {
        long long dx = a.x - b.x, dy = a.y - b.y;
        long long ans = gcd(dx,dy);
        if(ans)
        {
            dx /= ans;
            dy /= ans;
        }
        return dx* HASH_VALUE + dy;
    }
    int maxPoints(vector<Point>& points) {
        const int psz = points.size();
        int ans = (psz > 0);
        for(int i = 0; i < psz; i++)
        {
            unordered_map<long long,int> table;
            int duplicate = 0;
            for(int j = i + 1; j < psz; j++)
                if(points[i].x != points[j].x || points[i].y != points[j].y)
                {
                    long long rate = get_rate(points[i],points[j]);
                    if(table.count(rate))
                        table[rate] ++;
                    else
                        table[rate] = 2;
                }
                else
                    duplicate ++;
            if(ans <= duplicate)
                ans = duplicate + 1;
            for(const auto & term: table)
                if(term.second + duplicate > ans)
                    ans = term.second + duplicate;
        }
        return ans;
    }
};
```

**Complexity Analytics**

- Time Complexity: $$O(n^2)$$
- Space Complexity: $$O(n)$$
