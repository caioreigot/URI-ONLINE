import java.util.Scanner;

public class ID1072 {
    
    static Scanner input = new Scanner(System.in);

    public static void main(String args[]) {

        int in = 0, out = 0;
        int inputs = input.nextInt();

        int[] numbers = new int[inputs];
        for (int i = 0; i < inputs; i++) {
            numbers[i] = input.nextInt();
        }

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] >= 10 && numbers[i] <= 20) {
                in++;
            } else {
                out++;
            }
        }

        System.out.println(in + " in");
        System.out.println(out + " out");

    }

}