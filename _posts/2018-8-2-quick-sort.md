---
layout: page
title: Quick Sort
categories: [面试]
tags: [Algorithm, C++, quick sort]
excerpt: "链表快速归并排序和链表归并排序各种实现"
---


```cpp
#include <type_traits>
#include <iostream>
#include <vector>
#include <array>
#include <utility>
#include <list>
#include <forward_list>


template <typename RandomIt, typename  Compare=std::less<typename std::iterator_traits<RandomIt>::value_type> >
void quicksort(RandomIt first, RandomIt last, const Compare &comp = Compare()){
    if(first + 1 >= last)
        return;
    decltype((*first)) pivot = *first;
//    RandomIt ptr = first, now = first;
//    for(;now != last; ++now)
//        if(comp(*now, pivot))
//            std::swap(*(++ptr), *now);
//    std::swap(*first, *ptr);
//    quicksort(first, ptr, comp);
//    quicksort(ptr + 1, last, comp);

    RandomIt left = first, right = last;
    while(left < right){
        while(comp(pivot,*(--right)));
        while(left < right && comp(*(++left), pivot));
        //if(left < right)
            std::swap(*left, *right);
    }
    std::swap(*left, *first);
    quicksort(first, left, comp);
    quicksort(left + 1, last, comp);
}

/*
template <typename RandomIt>
void msort(RandomIt first, RandomIt last){
    using T = typename std::remove_reference<decltype(*first)>::type;
    quicksort<RandomIt, std::less<T>>(first, last, std::less<T>());
};
*/



template <typename T>
struct LinkNode {
    T value;
    LinkNode<T> * next;
    LinkNode():next(nullptr), value(){}
    LinkNode(const T & val, LinkNode<T> * lk):next(lk), value(val){}
};

template <typename T>
LinkNode<T> * __link_sort(LinkNode<T> * &first){
    if(first == nullptr || first->next == nullptr){
        return first;
    }
    LinkNode<T> *ptr = first->next, *tmp, *left = nullptr, *right = nullptr, *left_last=nullptr, *right_last=nullptr;
    while(ptr){
        tmp = ptr;
        ptr = ptr->next;
        if(tmp->value < first->value){
            tmp->next = left;
            left = tmp;
        }
        else{
            tmp->next = right;
            right = tmp;
        }
    }
    left_last = __link_sort(left);
    right_last = __link_sort(right);
    if(left_last != nullptr)
        left_last->next = first;
    else
        left = first;
    first->next = right;
    if(right == nullptr)
        right_last = first;
    first = left;
    return right_last;
}


template <typename T>
void link_sort(T & head){
    __link_sort(head);
}

template <typename T>
LinkNode<T> * __link_msort(LinkNode<T> *&head, std::size_t sz){
    if(sz <=  1){
        return head;
    }
    std::size_t left_sz = sz / 2, right_sz = sz - left_sz;
    LinkNode<T> new_head, * ptr = &new_head, * left = head;
    LinkNode<T> * left_last = __link_msort(left, left_sz);
    LinkNode<T> * right = left_last->next;
    LinkNode<T> * right_last = __link_msort(right, right_sz);
    LinkNode<T> * end_next = right_last->next;
    while(left_sz && right_sz){
        if(left->value < right->value) {
            ptr = ptr->next = left;
            left = left->next;
            left_sz--;
        }else{
            ptr = ptr->next = right;
            right = right->next;
            right_sz--;
        }
    }
    if(right_sz)
        left = right, left_last = right_last;
    if(left_sz || right_sz){
        ptr->next = left;
        ptr = left_last;
    }
    ptr->next = end_next;
    head = new_head.next;
    return ptr;
}

template <typename T>
void link_msort(T & head, std::size_t sz){
    __link_msort(head, sz);
}

template<typename T>
LinkNode<T> * __quick_sort(LinkNode<T> * &first){
    if(first == nullptr || first->next == nullptr)
        return first;
    LinkNode<T> lower, upper, *left = & lower, *right = & upper, * pov = first;
    first = first->next;
    while(first){
        if(pov->value < first->value){
            right->next = first;
            right = first;
        }
        else{
            left->next = first;
            left = first;
        }
        first = first->next;
    }
    left->next = right->next = nullptr;
    left = __quick_sort(lower.next);
    right = __quick_sort(upper.next);
    if(left == nullptr)
        left = &lower;
    left->next = pov;
    first = lower.next;
    pov->next = upper.next;
    if(right == nullptr)
        right = pov;
    return right;
}

template <typename T>
void list_qsort(T & head){
    __link_sort(head);
}

template <typename T>
LinkNode<T> * make_list(const std::vector<T> & values){
    LinkNode<T> head, * tmp = nullptr;
    for(const T & val:values){
        tmp = new LinkNode<T>(val, head.next);
        head.next = tmp;
    }
    return tmp;
}

template <typename T>
void print(LinkNode<T> * head){
    while(head){
        std::cout<<head->value << " ";
        head = head->next;
    }
    std::cout<<std::endl;
}

int testmsort(){
    test_vector();
    std::forward_list<int> ls;
    std::list<int> lst;
    ls.sort();
    lst.sort();
    std::vector<int> vec ={3,2,1,4,5,1,2,3,4,5,6,7,8,9,10};
    //std::vector<int> vec ={2,4,3,4};
    LinkNode<int> * first = make_list(vec), *last=nullptr;
    print(first);
    //link_msort(first, vec.size() - 6);
    /*  */

    link_sort(first);
//    link_qsort(first);
    print(first);
    return 0;
}

int __textmsort = testmsort();
int main(){
    return 0;
}

```
