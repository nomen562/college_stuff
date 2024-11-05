package com.codewithmosh.practise;

import java.util.*;

class Solution {
    public static String[] longestCommonPrefix(String[] strs) {
        String temp;
        for (int i = 0; i < strs.length; i++) {

            temp = strs[i];
            for (int j = i; j < strs.length; j++) {
                if (strs[j].compareTo(strs[j]) > 0) {
                    strs[i] = strs [j];
                    strs[j] = temp;
                }
            }


        }return strs;
    }

    public static void main(String[] args) {
        System.out.print(Arrays.toString(longestCommonPrefix(new String[]{"afsd", "asd", "asf"})));
    }
}