public class PatternRecursion {
    public static void main(String[] args) {
        printPattern(1, 4, 1);
    }

    static void printPattern(int start, int end, int spaces) {
        if (start > end) return;
        if (spaces < start) {
            System.out.print(" ");
            printPattern(start, end, spaces + 1);
        } else {
            System.out.print(spaces + " ");
            if (spaces < end) printPattern(start, end, spaces + 1);
            else {
                System.out.println();
                printPattern(start + 1, end, 1);
            }
        }
    }
}
