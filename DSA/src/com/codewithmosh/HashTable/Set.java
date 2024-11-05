package com.codewithmosh.HashTable;

import java.util.HashSet;

public class Set {
    public static void main(String[] args) {
        java.util.Set<Integer> set = new HashSet<>();
        int[] numbers = {1, 2, 3, 3, 4};
        for (int number : numbers)
            set.add(number);
        System.out.println(set);
    }
}
