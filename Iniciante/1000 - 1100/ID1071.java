import java.util.Scanner;

public class ID1071 {

    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {

        int start, end, sum = 0;

        start = in.nextInt();
        end = in.nextInt();

        if (start > end) {
            int temp = start;
            start = end;
            end = temp;
        }

        for (int i = start + 1; i < end; i++) {
            if (i % 2 != 0) {
                sum += i;
            }
        }

        System.out.println(sum);

    }

}