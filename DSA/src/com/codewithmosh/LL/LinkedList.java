package com.codewithmosh.LL;

import java.util.NoSuchElementException;

public class LinkedList {
    private int size;
    private class Node {
        private Node next;
        private int value;

        private Node(int value) {
            this.value = value;

        }
    }

    private Node first;
    private Node last;

    public void addLast(int item) {
        var node = new Node(item);

        if (isEmpty())
            first = last = node;
        else {
            last.next = node;
            last = node;
        }

        size++;
    }

    public void addFirst(int item) {
        var node = new Node(item);

        if (isEmpty())
            first = last = node;
        else {
            node.next = first;
            first = node;
        }

        size++;
    }
    private boolean isEmpty() {
        return first == null;
    }

    public int indexOf(int item) {
        int index = 0;
        var current= first;
        while (current != null) {
            if (current.value == item) return index;
            current = current.next;
            index++;
        }
        return -1;
    }

    public boolean contains(int item) {
        return (indexOf(item) != -1);
    }

    public void removeFirst() {
        if (isEmpty()) throw new NoSuchElementException();

        size--;

        if (first == last) {
            first = last = null;
            return;
        }

        var second = first.next;
        first.next = null;
        first = second;


    }

    public void removeLast() {
        if (isEmpty())
            throw new NoSuchElementException();

        size--;

        if(first == last) {
            return;
        }
        // [10 -> 20 -> 30]

        last = getPrevious(last);
        last.next = null;

    }

    private Node getPrevious(Node node) {
        var current = first;
        while (current != last  ) {
            if (current.next == last) return current;
            current = current.next;
        }
        return null;
    }

    public int size() {
        return size;
    }

    public int[] toArray() {
            int[] array = new int[size];
            var current = first;
            int index = 0;
            while (current != null) {
                array[index++] = current.value;
                current = current.next;
            }

            return array;
    }
    public void reverse() {
//        [10 -> 20 -> 30]
//        [10 <- 20 <- 30]
//        [10 ]
        if (isEmpty()) return;

        var previous = first;
        var current = first.next;
        while(current != null) {
            var next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }

        last = first;
        last.next = null;
        first = previous;
    }

    public int getKthNodeFromTheEnd(int k) {
        var a = first;
        var b = first;
        var current = first;

        for (int i = 0; i < k - 1; i++) {
            b = b.next;
            if (b.next == null)
                    throw new IllegalArgumentException("Not valid");
        }



        while (b != last) {
            a = a.next;
            b = b.next;
        }
        return b.value;
    }


}
