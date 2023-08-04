import java.util.Scanner;
import java.util.Arrays;

public class ConverteInteiros {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String linha = sc.nextLine();
		String[] strNums = linha.split(" ");
		int[] num = new int[strNums.length];

		for (int i = 0; i < strNums.length; i++) {
			num[i] = Integer.parseInt(strNums[i]);
		}

		System.out.println(Arrays.toString(num));


	}
}
