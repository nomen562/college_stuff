package com.codewithmosh.generics;
/* 
 * Declaring a class with multiple type parameters
 */
public class KeyValuePairs<K, V> {
    private K key;
    private V value;

    public KeyValuePairs(K key, V value) {
        this.key = key;
        this.value = value;
    }
    
}
