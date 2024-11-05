//package com.codewithmosh.mortgage;
//
//import java.io.PrintStream;
//import java.util.Scanner;
//
//public class Console {
//    private static Scanner scanner = new Scanner(System.in);
//
//    public static double readNumber(String prompt) {
//        System.out.print(prompt + scanner.nextDouble());
//    }
//
//    public static double readNumber(String prompt, int min, int max) {
//        double value;
//        System.out.print(prompt);
//        while(true) {
//            value = scanner.nextDouble();
//            if (value >= min && value <= max) break;
//            System.out.println("Please enter values between " + min + " and " + max);
//
//        }
//        return value;
//    }
//}