package practise;

import java.util.PriorityQueue;
import java.util.Queue;

public class PQ {
    public static void main(String[] args) {
        Queue<String> queue = new PriorityQueue<>();
        
        queue.offer("Hello");
        queue.offer("aqw");
        queue.offer("ZZlo");    
        queue.offer("qwello");

        while (!queue.isEmpty()) {
            System.out.println(queue.poll());
        }
    }
}
