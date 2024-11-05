package com.codewithmosh.LL;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        System.out.println(list.size());
        list.addLast(10);
        System.out.println(list.size());
        list.addLast(10);
        list.addLast(10);
        list.addLast(10);
        list.addFirst(100);
        list.addFirst(100);
        list.addFirst(100);
        list.removeFirst();
        list.removeLast();
        list.reverse();
        System.out.println(list.size());
        var array = list.toArray();
        System.out.println(Arrays.toString(array));
    }
}
