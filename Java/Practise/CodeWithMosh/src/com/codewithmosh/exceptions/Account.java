package com.codewithmosh.exceptions;

import java.io.IOException;

public class Account {
    public static void deposit(float value) throws IOException {
        if (value <= 0) 
            throw new IOException();
        
    }
}
