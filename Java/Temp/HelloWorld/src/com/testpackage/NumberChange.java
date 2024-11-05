package com.testpackage;

public class NumberChange {
    public static void main(String[] args) {
        int j = 1;
        for (int i = 1; i <= 6; i++) {
            for (int k = 1; k <= i; k++) {
                System.out.print(j + " ");
                j++;
            }
            System.out.println();
        }
    }
}
