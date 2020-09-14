import java.io.IOException;
import java.util.Scanner;

public class ID1067 {

	static Scanner in = new Scanner(System.in);
 
    public static void main(String[] args) throws IOException {
		
		int count = 1;
		int x = in.nextInt();
		
		if (x >= 1 && x <= 1000) {
			
			// Mostrar todos os nrs impares até x, incluindo x
			while (count <= x) {
				if (count % 2 != 0) {
					System.out.println(count);
				}
				count++;
			}
			
		} else {
			return;
		}
 
    }
 
}
