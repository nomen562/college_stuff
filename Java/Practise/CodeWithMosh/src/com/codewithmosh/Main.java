package com.codewithmosh;

import java.io.IOException;

import com.codewithmosh.exceptions.*;

public class Main {
    public static void main(String[] args) throws IOException {
    try {
        Account.deposit(1);
    } catch (IOException e) {
        // TODO Auto-generated catch block
        System.out.println("Logging....");
        throw e;
    }
    }
}