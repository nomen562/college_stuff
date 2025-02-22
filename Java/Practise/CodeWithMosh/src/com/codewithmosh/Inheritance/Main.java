package Inheritance;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        UIControl control = new UIControl(true);
        TextBox textBox = new TextBox();
        show(control);
    }
    public static void show(UIControl control) {
        var textbox = (TextBox) control;
        control.toString();
    }
}
