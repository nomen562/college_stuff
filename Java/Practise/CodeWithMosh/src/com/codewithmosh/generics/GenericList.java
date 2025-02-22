package com.codewithmosh.generics;

public class GenericList<T /* extends Number & Cloneable */ /*Here multiple interface and classes are declared. for cloning or copying a class */
 /* Number can me an iterface also */ /*suppose if the list can only store number
it is used to implment a constraint */
/* This constraint is called bounded type parameter as here T is restricted */
/* Under the hood, after compilation to java bytecode here all T's are converted 
to Object only 
if multiple constrainnsts then only the left most is considered
This is called type erasure
 */> {
    private T[] items = (T[]) new Object[10];
    private int count;

    public void add(T item) {
        items[count++] = item;
    }

    public T get(int index) {
        return items[index];
    }

}
