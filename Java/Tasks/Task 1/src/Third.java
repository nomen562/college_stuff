import java.util.Scanner;

public class Third {
    public static void main(String[] args) {

        System.out.print("Enter number>");
        int n = new Scanner(System.in).nextInt();

        System.out.println("Using For Loop");
        for (int i = 1; i <= 10; i++)
            System.out.println(n + " X " + i + " = " + (n * i));
        System.out.println("--------------");

        System.out.println("Using while loop");
        int i=1;
        while (i <= 10) {
            System.out.println(n + " X " + i + " = " + (n * i));
            i++;
        }
        System.out.println("--------------");

        System.out.println("Using do-while loop");
        i = 1;
        do {
            System.out.println(n + " X " + i + " = " + (n * i));
            i++;
        } while (i <= 10);
        System.out.println("--------------");
    }
}
