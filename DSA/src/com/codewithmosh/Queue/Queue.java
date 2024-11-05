package com.codewithmosh.Queue;

import java.util.Arrays;

public class Queue {
    // Array Dequeue
    // Array Enqueue
    // peek isEmpty isFull
    private int frontIndex;
    private int rearIndex;
    private int size;
    private int[] items;
    int count;

    public Queue(int size) {
    this.size = size;
    items = new int[size];
    }

    public void enqueue(int item) {
        if (rearIndex == size)
            throw new IllegalStateException("Full");
        items[rearIndex] = item;
        rearIndex = (rearIndex + 1) % size;
        count++;
    }

    public void dequeue() {
        if (frontIndex == rearIndex)
            throw new IllegalStateException("Empty");
        items[frontIndex] = 0;
        frontIndex = (frontIndex + 1) % size;
    }

    @Override
    public String toString() {
        return Arrays.toString(items);
    }

}
