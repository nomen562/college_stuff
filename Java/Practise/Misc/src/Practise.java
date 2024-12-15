import java.util.stream.Collectors;
import java.util.*;

public class Practise {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("2 lists are needed");
            throw new UnsupportedOperationException("Supply less than 2 lists");
        }

        List<Integer> firstSeries = Arrays.asList(args[0].split(",")).stream()
        .map(Integer::valueOf).toList();

        List<Integer> secondSeries = List.of(args[1].split(",")).stream()
        .map(Integer::valueOf).collect(Collectors.toList());

        System.out.println(firstSeries + ", " + secondSeries);
    }
}