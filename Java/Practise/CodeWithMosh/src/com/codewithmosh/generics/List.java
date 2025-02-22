package com.codewithmosh.generics;

public class List {
    private Object[] items;
    private int count;

    public List(int capacity) {
        items = new Object[capacity];
    }

    public void add(Object item) {
        items[count++] = item;
    }

    public Object get(int index) {
        return items[index];
    }
}
