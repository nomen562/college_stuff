package com.codewithmosh.Heap;

public class Heap {
    // int[] to store a list of integers
    // remove -> removes the root node
    // insert(int) -> inserts the int
    // for these two operations bubble up or down

    int items[] = new int[10];
    int size;

    public void insert(int value) {
        if (isFull())
            throw new IllegalStateException();

        items[size++] = value;
        bubbleUp();
    }

    public void remove() {
        if (isEmpty())
            throw new IllegalStateException();
        
        items[0] = items[--size];
        bubbleDown();
    }

    private boolean isFull() {
        return size == items.length;
    }

    private boolean isEmpty() {
        return size == 0;
    }

    private void bubbleUp() {
        var index = size - 1;
        while (index > 0 && items[index] > items[parent(index)]) {
            swap(index, parent(index));
            index = parent(index);
        }
    }

    private void bubbleDown() {
        var index = 0;
        while (index < size && !isValidParent(index)) {
            var largerChildIndex = largerChildIndex(index);
            swap(index, largerChildIndex);
            index = largerChildIndex;
        }
    }

    private boolean isValidParent(int index) {
        return (items[index] >= leftChild(index) || 
        items[index] >= rightChild(index));
    }

    private int parent(int index) {
        index = (index - 1) / 2;
        return index;
    }

    private int leftChildIndex(int index) {
        return 2 * index + 1;
    }

    private int rightChildIndex(int index) {
        return 2 * index + 2;
    }

    private int largerChildIndex(int index) {
        return (leftChild(index) > rightChild(index)) ?
                leftChildIndex(index) :
                rightChildIndex(index);
    }

    private int leftChild(int index) {
        return items[leftChildIndex(index)];
    }

    private int rightChild(int index) {
        return items[rightChildIndex(index)];
    }

    private void swap(int first, int second) {
        var temp = items[first];
        items[first] = items[second];
        items[second] = temp;
    }
}
