package com.codewithmosh;

import java.util.Arrays;
import java.util.LinkedList;

public class Lnk {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        list.addLast(10);
        list.addLast(10);
        list.addLast(10);
        System.out.println(list.contains(10) + " " + list.indexOf(10));
        list.add(2, 100);
        System.out.println(list);
        list.get(3);

    }
}
