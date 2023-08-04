/**
 * Laboratório de Programação 2 - Lab 1
 *
 * @author Carmelita Braga de Araújo Medeiros - 121210008
 */

import java.util.Scanner;

public class FuncaoMonotona {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();

		if (a > b && b > c && c > d) {
			System.out.println("POSSIVELMENTE ESTRITAMENTE DECRESCENTE");
		} else if (a < b && b < c && c < d) {
			System.out.println("POSSIVELMENTE ESTRITAMENTE CRESCENTE");
		} else {
			System.out.println("FUNCAO NAO ESTRITAMENTE CRES/DECR");
		}
	}
}
