package com.codewithmosh.Tree;

public class BinaryTree {
    private class Node {
        private int value;
        private Node leftChild;
        private Node rightChild;

        public Node(int value) {
        this.value = value;
        }

        @Override
        public String toString() {
            return "Node = " + value;
    }
    }

    private Node root;
    public void insert(int value) {
         if (root == null) {
             root = new Node(value);
             return;
         }

         var current = root;
         while (true) {
             if (value < current.value) {
                 if (current.leftChild == null) {
                     current = new Node(value);
                     break;
                 }
                 current = current.leftChild;
             }
             else
                 current = current.rightChild;
         }
    }




}
