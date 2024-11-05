import java.util.Arrays;
import java.util.Scanner;

public class Question1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter words separated by space: ");
        String sentence = scanner.nextLine();
        String[] words = sentence.split(" ");

        int l = 0;
        for (String word : words)
            l += word.length();
        System.out.println("Total length is: " + l);
    }
}
