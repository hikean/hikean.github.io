---
layout: page
title: 堆排序以及优先队列
categories: [面试]
tags: [Algorithm, C++, heap sort, heap, priority_queue]
excerpt: "堆排序以及优先队列"
---


```cpp

#include <iostream>

using std::swap;
template<typename T>
void heap_up(T & container, int cnt, int pos = 0){
    if(pos == 0)
        pos = cnt - 1;
    while(pos > 0 && container[pos] > container[(pos -1)/2]){
        swap(container[pos], container[(pos-1)/2]);
        pos = (pos - 1) / 2;
    }
}

template<typename T>
void heap_down(T & container, int cnt, int pos = 0){
    while(true){
        int left = pos * 2 + 1, right = pos * 2 + 2, index = pos;
        if(left < cnt && container[index] < container[left])
            index = left;
        if(right < cnt && container[index] < container[right])
            index = right;
        if(index == pos) break;
        swap(container[pos], container[index]);
        pos = index;
    }
}
template<typename T, typename V>
V heap_pop(T container, int cnt){
    swap(container[0], container[cnt -1]);
    heap_down(container, cnt -1);
    return container[cnt -1];
}
template<typename T, typename V>
int heap_push(T & container, int cnt, const V & value){
    container[cnt] = value;
    heap_up(container, cnt+1);
    return cnt + 1;
}
template<typename T>
void heap_build(T & container, int cnt){
    for(int root = (cnt - 2)/2; root >= 0; --root)
        heap_down(container, cnt, root);
}
template<typename T>
void heap_sort(T & container, int cnt){
    heap_build(container, cnt);
    //std::for_each(container.begin(), container.end(), [](const int & a){std::cout << a << " ";}); std::cout<<std::endl;
    for(int i = cnt - 1; i > 0; i--){
        std::swap(container[0], container[i]);
        heap_down(container, i, 0);
    }
}
#include <vector>
// #include <initializer_list>
template <typename T, typename Comp=std::less<T> >
class Heap{
    std::vector<T> datas;
    Comp comp;
    void build();
    void up(int pos);
    void down(int pos);
public:
    explicit Heap(const Comp & cmp=Comp()):comp(cmp){
        //std::cout<<"0 default construct" <<std::endl;
    }
    explicit Heap(const std::vector<T> & vec, const Comp & cmp=Comp()):datas(vec), comp(cmp){
        build();
        //std::cout<<"1 vector construct"<<std::endl;
    }
    explicit Heap(std::vector<T> && vec, const Comp & cmp=Comp()) noexcept :datas(vec), comp(cmp) {
        build();
        //std::cout<<"2 vector move construct"<<std::endl;
        // can be called as Heap<int> h({1,2,2}); without explicit
    }
    Heap(std::initializer_list<T> ilist, const Comp & cmp=Comp()):datas(ilist.begin(),ilist.end()), comp(cmp){
        build();
        //std::cout<<"3 list construct"<<std::endl;
        // can be called as Heap<int> a = {1,2,3}, b({2,3,4}), c{1,2,3,4};
    }
    template <typename Input>
    Heap(Input first, Input last, const Comp & cmp=Comp()):datas(first, last), comp(cmp){
        build();
        //std::cout<<"4 range construct" << std::endl;
    }
    Heap(Heap && h) noexcept :datas(std::move(h.datas)), comp(h.comp){ // 1
        //std::cout<<"5 move copy construct"<<std::endl;
        // can be called as Heap<int> h(std::move(hx)), h2 = std::move(hn);
    }
    Heap(const Heap & h):datas(h.datas), comp(h.comp){ // 2
        //std::cout<<"6 copy construct" << std::endl;
        // can be called as Heap<int> h(hx), h2 = hn;
    }
    Heap & operator = (const Heap & h){  // 3
        //std::cout<<"7 assignment copy" << std::endl;
        this->datas = h.datas;
        return *this;
        // be called as Heap<int> h1, h2; h1 = h2;
    }

    Heap & operator = (Heap && h) noexcept { // 4
        //std::cout<<"8 move assignment copy" << std::endl;
        this->datas = move(h.datas);
        return *this;
        // be called as Heap<int> h1, h2; h1 = std::move(h2); h2 = Heap<int>{};
    }
    ~Heap(){
        //std::cout<<"destruct Heap\n";
    }; // 5
    T top();
    void push(const T & v);
    void pop();
    bool empty();
    template <typename ... V> void emplace(V ... args){
        datas.emplace_back(args...);
        Heap<T, Comp>::up((int)datas.size() - 1);
    }
};

template <typename T, typename Comp>
void Heap<T, Comp>::up(int pos){
    while(pos > 0 && comp(datas[(pos-1)/2], datas[pos]))
    {
        std::swap(datas[pos], datas[(pos - 1)/2]);
        pos = (pos - 1) / 2;
    }
}

template <typename T, typename Comp>
void Heap<T, Comp>::down(int pos){
    while(true){
        int left = pos * 2 + 1, right = pos * 2 + 2, maxi = pos;
        if(left < datas.size() && comp(datas[maxi], datas[left]))
            maxi = left;
        if(right < datas.size() && comp(datas[maxi], datas[right]))
            maxi = right;
        if(maxi == pos) break;
        std::swap(datas[pos], datas[maxi]);
        pos = maxi;
    }
}

template <typename T, typename Comp>
T Heap<T, Comp>::top(){
    return datas[0];
}

template <typename T, typename Comp>
void Heap<T, Comp>::pop(){
    datas[0] = datas.back();
    datas.pop_back();
    Heap<T, Comp>::down(0);
}

template <typename T, typename Comp>
void Heap<T, Comp>::push(const T & v){
    datas.push_back(v);
    Heap<T, Comp>::up((int)datas.size() - 1);
}

template <typename T, typename Comp>
void Heap<T, Comp>::build(){
    for(int root = (int(datas.size()) - 2) / 2; root >= 0; root--)
        Heap<T, Comp>::down(root);
    //std::for_each(datas.begin(), datas.end(), [](const T & x){std::cout << x <<" ";}); std::cout << std::endl;
}

template <typename T, typename Comp>
bool Heap<T, Comp>::empty(){
    return datas.size() == 0;
}

Heap<int> htest(int x){
    Heap<int> h1;
    h1.emplace(x);
    return h1;
}

int test_heap(){
    std::vector<int> vec{3,4,5,6,7,89,1,2,3}, v2{3,4,5,6};
    Heap<int> h0, h7, h8;
    Heap<int> h1(vec);//, h11 = vec;
    //h0 = vec ;// 1 8
    Heap<int> h2(std::vector<int>{1,2,3}), h22(std::move(v2)); // 2
    Heap<int> h3={3,4,5}, h33({3,4,2,0}), h333{3,4,5,6}, h3333(Heap<int>{1,2,3});
    h3333 = Heap<int>();
    Heap<int> h4(vec.begin(), vec.end());
    //Heap<int> h5 = std::move(h2), h55(std::move(h1));下　
    Heap<int> h6 = h4, h66(h4);
    h7 = h4;
    h8 = std::move(h7);
    h8 = Heap<int>();
    std::cout<<"\ndone!\n";
    Heap<int> ht = htest(vec.size());
    Heap<int, std::greater<int>> h(vec);
    for(const auto &x:vec) h.emplace(x);
    while(!h.empty())
    {
        std::cout << h.top() << " ";
        h.pop();
    }
    return 0;
}
//int __heapmain = test_heap();

int mhsort(){
    std::vector<int> vec{9,3,4,5,6,7,0,2};
    heap_sort(vec, (int)vec.size());
    std::for_each(vec.begin(), vec.end(), [](const int & a){std::cout << a << " ";}); std::cout<<std::endl;
    return 0;
}
//int __mhsort = mhsort();

int main(){
    return 0;
}

```
