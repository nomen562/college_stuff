import java.util.Scanner;

public class Second {
    public static void main(String[] args) {
        System.out.print("Enter your number>");
        int n = new Scanner(System.in).nextInt();

        int s = 0;
        System.out.println("Using For Loop");
        for (int i = 1; i <= n; i++)
            s += i;
        System.out.println("Sum of n numbers: " + s);
        System.out.println("--------------------");

        System.out.println("Using While Loop");
        s = 0;
        int i = 1;
        while (i <= n) {
            s += i;
            i++;
        }
        System.out.println("Sum of n numbers: " + s);
        System.out.println("--------------------");

        System.out.println("Using Do-While Loop");
        s = 0;
        i = 1;
        do {
            s += i;
            i++;
        }
        while (i <= n);
        System.out.println("Sum of n numbers: " + s);
        System.out.println("--------------------");
    }
}
