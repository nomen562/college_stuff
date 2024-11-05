package com.codewithmosh;


import java.util.LinkedList;

public class KNode {
    public static void main(String[] args) {
        //Find the Kth node from the end in a linked list in one pass
        // i.e. you dont know the total number of elements

        // [10 -> 20 -> 30 -> 40 -> 50 -> 60]
        // [                   *           *]
        // k = 3 distance = 2
        // we need two pointer that are k-1 apart
        // move the second pointer until it is at the right distance from the first pointer
        // then move both of them forward until the second pointer reaches the end
        LinkedList<Integer> list = new LinkedList<>();
        list.addLast(10);
        list.addLast(10);
        list.addLast(10);
        list.addFirst(100);
        list.addFirst(100);
        list.addFirst(100);


    }
}
