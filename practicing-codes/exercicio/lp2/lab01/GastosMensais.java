/**
 * @author Carmelita Braga
 */

import java.util.*;
import java.util.Arrays;

public class GastosMensais {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String[] meses = sc.nextLine().split(" ");
		int[] gastosMensais = new int[12];

		for (int i = 0; i < 12; i++) {
			gastosMensais[i] = sc.nextInt();
		}
		int idx = -1;
		String mes = sc.next();

		for (int j = 0; j < meses.length; j++) {
			if (meses[j].equals(mes)) {
				idx = j;
			}
		}

		System.out.println(gastosMensais[idx]);
	}
}
