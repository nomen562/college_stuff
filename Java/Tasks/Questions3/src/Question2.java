import java.util.Scanner;

public class Question2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the sentence: ");
        String sentence = scanner.nextLine();
        System.out.print("Enter character to be replaced: ");
        char toReplace = scanner.next().charAt(0);
        System.out.print("Enter character replacement: ");
        char replacement = scanner.next().charAt(0);

        StringBuilder newSentence = new StringBuilder();
        for (int i = 0; i < sentence.length(); i++) {
            if (sentence.charAt(i) == toReplace)
                newSentence.append(replacement);
            else
                newSentence.append(sentence.charAt(i));
        }
        System.out.println("The new sentence is: " + newSentence);
    }
}
