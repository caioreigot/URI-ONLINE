import java.io.IOException;
import java.util.Scanner;

public class ID1065 {

	static Scanner in = new Scanner(System.in);
 
    public static void main(String[] args) throws IOException {

		int numero, qntPares = 0;
		
		for (int i = 0; i < 5; i++) {
			numero = in.nextInt();
			
			if (numero % 2 == 0) {
				qntPares++;
			}
			
		}
		
		System.out.println(qntPares + " valores pares");
 
    }
 
}