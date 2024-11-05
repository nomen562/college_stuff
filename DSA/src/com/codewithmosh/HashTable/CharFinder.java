package com.codewithmosh.HashTable;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class CharFinder {
    public char findFistNonRepeatingchar(String str) {
        HashMap<Character, Integer> map = new HashMap<>();

        char[] chars = str.toCharArray();

        for (char ch : chars) {
            var count = map.containsKey(ch) ? map.get(ch) : 0;
            map.put(ch, count + 1);
        }

        for (char ch : chars)
            if (map.get(ch) == 1) return ch;

        return Character.MIN_VALUE;
    }

    public char firstRepeatedCharacter(String str) {
        Set<Character> set = new HashSet<>();

        for (var ch : str.toCharArray()) {
            if (set.contains(ch)) return ch;

            set.add(ch);
        }
        
        return Character.MIN_VALUE;
    }

}
