public class Pattern1 {
    public static void main(String[] args) {
        int i = 3;
        int flag=1;

        do {
            if (i < 0) i = 3;

            for (int j = 0; j < i ; j++)    //print 'i' spaces
                System.out.print(" ");

            for (int j = 0; j <= 2*(3-i); j++)  //print
                System.out.print("*");

            System.out.println();

            if (i == 0) flag--;
            if (flag == 1) i--;
            else i++;

        } while(i <= 3);
    }
}
