package com.codewithmosh.generics;

/* 
 * We want the Instructor class to inherit from the User class
 * But out instructor class doesnt know what inital value(points) to pass/ argument to pass to the constructor of the
 * User class. 
 */
public class Instructor extends User{
    // To solve this problem we use a custom constructor and pass that value to the constructor of the base class using super keyword
    public Instructor(int points) {
        super(points);
    }
}
