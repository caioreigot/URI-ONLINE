import java.util.Scanner;

public class ID1073 {
    
    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {

        int end = in.nextInt();

        for (int i = 0; i <= end; i++) {
            if (i % 2 == 0 && i != 0) {
                System.out.println(i+"^2 = " + (int)Math.pow(i, 2));
            }
        }

    }

}
