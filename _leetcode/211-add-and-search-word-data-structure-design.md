---
layout: leetcode
date: 2016-07-16
title: Add and Search Word - Data structure design
tags: [Backtracking, Trie, Design]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Design a data structure that supports the following two operations:

      void addWord(word)
      bool search(word)

 search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

**For example:**

<pre>
      addWord("bad")
      addWord("dad")
      addWord("mad")
      search("pad") -> false
      search("bad") -> true
      search(".ad") -> true
      search("b..") -> true
</pre>

 **Note:**

You may assume that all words are consist of lowercase letters `a-z`.


***

## Solution

**Result:** Accepted **Time:** 84 ms

Here should be some explanations.

```cpp
struct Node{
    bool exist;
    Node * nodes[26]={0};
    Node(const bool & e=false):exist(e){}
    Node * & get_node(const char & a)
    {
        return nodes[a-'a'];
    }
    const Node * get_node(const char & a) const
    {
        return nodes[a-'a'];
    }
};
class WordDictionary {
public:
    Node root;
    void addWord(string word) {
        Node * tmp = &root;
        for(const auto & c:word)
        {
            if(!tmp->get_node(c))
                 tmp->get_node(c) = new Node();
            tmp= tmp->get_node(c);
        }
        tmp->exist = true;
    }
    bool srch(const Node * now,const char *ptr)
    {
        if(now == NULL || *ptr == '\0')
            return now && now->exist;
        if(*ptr!='.')
            return srch(now->get_node(*ptr),ptr+1);
        else
             for(char c = 'a'; c <='z'; c++)
                if(srch(now->get_node(c),ptr+1))
                    return true;
        return false;
    }


    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    bool search(string word) {
         return srch(&root,word.c_str());
    }
};

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary;
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
