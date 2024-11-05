package com.codewithmosh.Queue;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
//        Queue<Integer> queue = new ArrayDeque<>();
//        queue.add(10);
//        queue.add(20);
//        queue.add(30);
//        System.out.println(queue);
//        reverse(queue);
//        System.out.println(queue);
        var queue2 = new com.codewithmosh.Queue.Queue(5);
        queue2.enqueue(12);
        queue2.enqueue(13);
        queue2.enqueue(14);
        queue2.enqueue(14);
        queue2.enqueue(14);
        System.out.println(queue2.toString());

        var pq = new PriorityQueue(6);
        pq.add(6);
        pq.add(1);
        pq.add(3);
        System.out.println(pq.toString());


    }
    public static void reverse(Queue<Integer> queue) {
//        only using add remove empty
        var stack = new Stack<Integer>();
        while (!queue.isEmpty()) {
            stack.push(queue.remove());
        }
        while (!stack.isEmpty()) {
            queue.add(stack.pop());
        }
    }

}
