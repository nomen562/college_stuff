import java.util.Scanner;

public class Fourth {
    public static void main(String[] args) {
        System.out.print("Enter date>");
        int date = new Scanner(System.in).nextInt();
        String holiday = whatHoliday(date);

        System.out.println(holiday);
    }
    public static String whatHoliday(int date) {
        if (date < 16 && date > 12) return "Pongal Holidays";
        if ((date + 1) % 7 == 0) return "Holiday (Saturday)";
        if (date % 7 == 0)  return "Holiday (Sunday)";  //Weekdays
        if (date == 26) return "Republic Day";
        else return "Not a Holiday";

    }
}
