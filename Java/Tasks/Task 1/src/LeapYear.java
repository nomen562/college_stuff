import java.util.Scanner;

public class LeapYear {
    public static void main(String[] args) {
        System.out.print("Enter year>");
        short year = new Scanner(System.in).nextShort();

        if (year % 4 == 0) {
            if (year % 100 == 0)
                if ( year % 400 == 0)
                System.out.println("Leap year");
                else System.out.println("Not a leap year");
            else System.out.println("Leap year");
        }
        else System.out.println("Not a leap year");



//        if (year % 100 == 0 && year/100 % 4 == 0)
//            System.out.println("Leap year");
//        else if (year % 100 != 0 && year % 4 == 0)
//            System.out.println("Leap Year");
//        else System.out.println("Not a leap year");

    }
}
