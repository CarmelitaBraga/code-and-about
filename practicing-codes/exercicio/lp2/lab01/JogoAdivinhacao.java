import java.util.*;

public class JogoAdivinhacao {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int numero = sc.nextInt();
		int tent = sc.nextInt();

		while (tent != numero) {

			if (tent > numero) {
				System.out.println("MAIOR");
			} else {
				System.out.println("MENOR");
			}

			tent = sc.nextInt();
		}

		System.out.println("ACERTOU");
	}
}
