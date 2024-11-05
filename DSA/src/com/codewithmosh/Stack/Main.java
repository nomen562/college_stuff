package com.codewithmosh.Stack;

public class Main {
    public static void main(String[] args) {
        var stack = new Stack(5);
        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.pop();
        stack.pop();
        System.out.println(stack.peek());
    }
}