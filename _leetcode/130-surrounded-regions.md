---
layout: leetcode
date: 2016-07-13
title: Surrounded Regions
tags: [Union Find, Breadth First Search]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

> Given a 2D board containing `'X'` and `'O'` (the letter O), capture all regions surrounded by `'X'`.
>
>A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.
>
>For example,
>
>     X X X X
>     X O O X
>     X X O X
>     X O X X
>
>After running your function, the board should be:
>
>     X X X X
>     X X X X
>     X X X X
>     X O X X
>
>    

***

## Solution

**Result:** Accepted **Time:** 8 ms

Here should be some explanations.

```c
int stck[655350],top;
void dfs(int x,int y,char ** board,const int row,const int col,const char tag)
{
    top = 0;
    stck[top++] = x; stck[top++] = y;
    while(top)
    {
        y = stck[--top]; x = stck[--top];
        if(board[x][y] != 'O')
            continue;
        board[x][y] = tag;
        if(y > 0)
            {stck[top++] = x; stck[top++] = y - 1;}
        if(y < col - 1)
            {stck[top++] = x; stck[top++] = y + 1;}
        if(x > 0)
            {stck[top++] = x - 1; stck[top++] = y;}
        if(x < row - 1)
            {stck[top++] = x + 1; stck[top++] = y;}
    }
}
void solve(char** board, int row, int col) {
    for(int i = 0; i < row; i++)
        dfs(i,0,board,row,col,'#'),dfs(i,col-1,board,row,col,'#');
    for(int j = 0; j < col; j++)
        dfs(0,j,board,row,col,'#'),dfs(row-1,j,board,row,col,'#');
    for(int i = 1; i < row - 1; i++)
        for(int j = 1; j < col - 1; j++)
            dfs(i,j,board,row,col,'X');
    for(int i = 0; i < row; i++)
        for(int j = 0; j < col; j++)
            if(board[i][j] == '#')
                board[i][j] = 'O';
}
```

**Complexity Analytics**

- Time Complexity: $$O(n*n)$$
- Space Complexity: $$O(n)$$
