import java.io.IOException;
import java.util.Scanner;

public class ID1066 {
 
	static Scanner in = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
 
		int pares = 0, impares = 0, positivos = 0, negativos = 0;
		
		for (int i = 0; i < 5; i++) {
			
			int numero = in.nextInt();
			
			// Par ou impar
			if (numero % 2 == 0) {
				pares++;
			} else {
				impares++;
			}
			
			if (numero != 0) {
				// Positivo ou negativo
				if (numero > 0) {
					positivos++;
				} else {
					negativos++;
				}
			}
			
		}
		
		System.out.println(pares + " valor(es) par(es)");
		System.out.println(impares + " valor(es) impar(es)");
		System.out.println(positivos + " valor(es) positivo(s)");
		System.out.println(negativos + " valor(es) negativo(s)");
		
	}
 
}
