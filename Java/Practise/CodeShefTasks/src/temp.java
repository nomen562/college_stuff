
public class temp {
    public static void main(String[] args) {
        System.out.println(swap("hello my name is rishit malik and what is your name and what ", 1, 10));
    }
    public static String swap(String s, int i, int j) {
        char t;
        char[] chars = s.toCharArray();
        t = chars[i];
        chars[i] = chars[j];
        chars[j] = t;
        return new String(chars);
    }
}
