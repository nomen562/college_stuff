package com.codewithmosh.exceptions;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.NoSuchFileException;
import java.text.ParseException;
import java.text.SimpleDateFormat;

public class ExceptionsDemo {
    public static void show() {

        try (
            var reader = new FileReader("null");
            
        ) {
            reader.read();
            
        }
        catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}