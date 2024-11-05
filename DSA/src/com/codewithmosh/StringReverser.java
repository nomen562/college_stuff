package com.codewithmosh;

import java.util.Stack;

public class StringReverser {
    public String StringReverser(String input) {

        if (input == null)
            throw new IllegalArgumentException(); //Use this if using any method on a string
        Stack<Character> stack = new Stack<>();

//        for (int i = 0; i < input.length(); i++)
//            stack.push(input.charAt(i));
        for (char character : input.toCharArray())
            stack.push(character);

        StringBuilder reversed = new StringBuilder();
        while (!stack.empty())
            reversed.append(stack.pop());
        return reversed.toString();
    }
}
