import java.util.Scanner;

public class ID1070 {
    
    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {

        int x = in.nextInt();
        int count = 0;

        while (count != 6) {
            if (x % 2 != 0) {
                System.out.println(x);
                count++;
            }
            
            x++;

        }
    }
}
