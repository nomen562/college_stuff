package com.codewithmosh.Heap;

public class Main {
    public static void main(String[] args) {
        var heap = new Heap();
        heap.insert(16);
        heap.insert(3);
        heap.insert(17);
        heap.insert(18);
        System.out.println("First");
        heap.remove();
        heap.remove();
        heap.remove();
        heap.insert(10);
        heap.insert(20);
    }
}
