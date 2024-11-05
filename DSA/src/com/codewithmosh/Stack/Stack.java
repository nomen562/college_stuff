package com.codewithmosh.Stack;

import java.util.Arrays;

public class Stack {
    private int[] items;
    private int currentIndex;
    private int size;

    public Stack(int size) {
        this.size = size;
        items = new int[size];
    }

    public void push(int item) {
        if (currentIndex == size)
            throw new StackOverflowError("Stack is full");

        items[currentIndex++] = item;
    }

    public int pop() {
        if (currentIndex == 0)
            throw new IllegalStateException("Stack is empty");

        return items[--currentIndex];
    }

    public int peek() {
        if (currentIndex == 0)
            throw new IllegalStateException("Cant peek");
        return items[currentIndex - 1];
    }

    public boolean isEmpty() {
        return currentIndex == 0;
    }

    @Override
    public String toString() {
        var content = Arrays.copyOfRange(items, 0, currentIndex);
        return Arrays.toString(content);
    }
}
