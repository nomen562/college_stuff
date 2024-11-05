package com.codewithmosh.Stack;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class Expression {
    private static List<Character> leftBrackets = Arrays.asList('(', '[', '{');
    private String input;
    public Expression(String input) {
        this.input = input;
    }
    public boolean isEqual() {
        Stack<Character> stack = new Stack<>();

        for (char ch : input.toCharArray()) {
            if (isRightBracket(ch)) {
                if (stack.isEmpty()) return false;
                var top = stack.pop();
                if (doBracketsMatch(ch, top)) return false;
            }

            if (isLeftBracket(ch))
                stack.push(ch);
        }

        return stack.empty();
    }

    private static boolean isRightBracket(char ch) {
        return ch == ')' || ch == ']' || ch == '}' || ch == '>';
    }

    private static boolean isLeftBracket(char ch) {
        return ch == '(' || ch == '[' || ch == '{' || ch == '<';
    }

    private static boolean doBracketsMatch(char left, Character top) {
        return (left == ')' && top != '(') ||
                (left == ']' && top != '[') ||
                (left == '}' && top != '{') ||
                (left == '>' && top != '<');
    }
}
