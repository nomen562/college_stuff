package com.codewithmosh.Queue;

import java.util.Arrays;

public class PriorityQueue {
//    [1, 3, 7, 21]
//    [1, 2 ]
    private int[] items;
    private int count;

    public PriorityQueue(int size) {
        items = new int[size];
    }

    public void add(int item) {
        int i;
        for (i = count - 1; i >= 0; i--)
            if (items[i] > item)
                items[i+1] = items[i];
            else
                break;

        items[i+1] = item;
        count++;
    }

    @Override
    public String toString() {
        return Arrays.toString(items);
    }
}
