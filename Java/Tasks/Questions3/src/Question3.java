import java.util.Scanner;

public class Question3 {
    public static void main(String[] args) {
        System.out.print("Enter email>");
        String email = new Scanner(System.in).nextLine();
        String username = email.substring(0, email.indexOf('@'));
        System.out.println("The username is: " + username);
    }
}
