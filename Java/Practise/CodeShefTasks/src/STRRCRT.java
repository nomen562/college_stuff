import java.util.Scanner;

public class STRRCRT {
    public static void main(String[] args) {
        char[] chef = new char[] {'C', 'O', 'O', 'K', 'O', 'F', 'F'};
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter s1: ");
        String s1 = scanner.next();
        System.out.print("Enter s2: ");
        String s2 = scanner.next();

    }
    public static String[] permutations(String s) {
            int length = s.length();
            String[] res = new String[factorial(length)];

        }
    public static String permutation(String s) {
        var l = s.length();
        for (int i = 0; i < l; i++) {
            s = swap()
        }
    }
    public static String swap(String s, int i, int j) {
        char t;
        char[] chars = s.toCharArray();
        t = chars[i];
        chars[i] = chars[j];
        chars[j] = t;
        return new String(chars);
    }
    public static int factorial(int n) {
        return n < 2 ? 1 : n * factorial(n-1);
    }
}
