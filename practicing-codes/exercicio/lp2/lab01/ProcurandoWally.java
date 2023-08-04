/**
 * Laboratório de Programação 2 - Lab 01
 *
 * @author Carmelita Braga - 121210008
 */

import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class ProcurandoWally {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		ArrayList<String> tamIgual = new ArrayList<String>();

		while (true) {
			String nomesw = sc.nextLine();
			String[] nomes = nomesw.split(" ");

			if (nomesw.contains("wally")) {
				break;
			}

			boolean existencia = false;
			int tam = nomes.length;

			for (int i = tam-1; i > -1; i--) {
				if (nomes[i].length() == 5) {
					tamIgual.add(nomes[i]);
					existencia = true;
					break;
				}
			}
			if (existencia == false) {
				tamIgual.add("?");
			}
		}

		int tamF = tamIgual.size();
		for (int j = 0; j < tamF; j++) {
				System.out.println(tamIgual.get(j));
		}

	}
}
