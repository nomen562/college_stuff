package com.codewithmosh.generics;

public class Utils {
    /*
     * We can also declare generic methods in a non generic class 
     * for example here in utils
     * Common convennction for utility methods is to declare them static
     * 
     */


    //  public static int max(int first, int second) {
    //     return (first > second) ? first : second;
    //  }

    /*
     * Now we want to make this method generic that instead of getting
     * two integers and returning one integer we want to be able to work
     * with different types of object. Instead of making this Utils class
     * generic we can declare a non generic method in a non generic class
     * add <T> before datatype and replace all int (datatypes) with T
     */

    public static <T extends Comparable<T>> T max(T first, T second) {
        return (first.compareTo(second) > 0) ? first : second;
    }
/* 
 * Declare multiple type parameters
 * By convenction when we have 2 type paramenter we use K and V for key and value
 * initially the java compiler sees both these parameters as objects.
 */
    public static <K extends Number, V> void print(K key, V value) {
        System.out.println(key + " = " + value);
    }

    public static void printUser(User user) {
        System.out.println(user);
    }

    // public static void printUsers(GenericList<User> users) {

    // }
    // we replace the type argument with a ? which is a wilcard character
    // this wildcard represents an unknown type
    // With wildcards we can cast generic type

    // class CAP#1 extends User
    // class Instructor extends User
    public static void printUsers(GenericList<? extends User> users) {
        // Now we can pass anything even Integer objects but we cant treat them as user objects
        // When we use a wlidcard the java compiler is going to create an anonymous type under the hood
        // class CAP#1 created. #1 stands for the first type
        users.get(1);
        users.get(1);
        // get method returns an instance of the Capture class that means we can only store it in the type Cap or its base type
        Object x = users.get(1);
    }

    public static void main(String[] args) {
        System.out.println();
    }
} 
