---
layout: leetcode
date: 2016-07-16
title: Implement Trie (Prefix Tree)
tags: [Design, Trie]
---

* Contents
{:toc #toc_of_keans_blog}

## Question

 Implement a trie with `insert`, `search`, and `startsWith` methods.

**Note:**

You may assume that all inputs are consist of lowercase letters `a-z`.


***

## Solution

**Result:** Accepted **Time:** 64 ms

Here should be some explanations.

```cpp
class TrieNode {
public:
    // Initialize your data structure here.
    bool exist;
    TrieNode* nodes[26]={0};
    TrieNode():exist(false){}
    TrieNode * & getNode(const char & chr)
    {
        return nodes[chr-'a'];
    }
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(const string & word) {
        TrieNode * now = root;
        for(const auto &x:word)
           if(!now->getNode(x))
                now = now->getNode(x) = new TrieNode();
            else
                now = now->getNode(x);
        now->exist = true;
    }

    // Returns if the word is in the trie.
    bool search(const string & word) {
         TrieNode * now = root;
        for(const auto &x:word)
                if(!(now = now->getNode(x)))
                    return false;
        return now->exist;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(const string & prefix) {
         TrieNode * now = root;
        for(const auto &x:prefix)
                if(!(now = now->getNode(x)))
                    return false;
        return true;
    }
private:
    TrieNode* root;
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");
```

**Complexity Analytics**

- Time Complexity: $$O(n)$$
- Space Complexity: $$O(1)$$
