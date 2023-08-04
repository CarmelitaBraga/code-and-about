/**
 * Laboratório de Programação 2 - Lab 1
 *
 * @author Carmelita Braga de Araújo Medeiros - 121210008
 */

import java.util.Scanner;

public class MaiorMenorde5 {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		String palavra1 = sc.next();
		String maior = palavra1;
		String menor = palavra1;

		for (int i = 1; i < 5; i++) {
			String palavra = sc.next();
			
			if (palavra.length() > maior.length()) {
				maior = palavra;
			}
			if (palavra.length() < menor.length()) {
				menor = palavra;
			}
		}

		System.out.println(menor);
		System.out.println(maior);


	}
}
