import java.util.*;

public class PalavrasPoeticas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String palavra1 = sc.next();
        int tam1 = palavra1.length();
        char letraInicial1 = palavra1.charAt(0);
        char letraFinal1 = palavra1.charAt(tam1 - 1);

        String palavra2 = sc.next();
        int tam2 = palavra2.length();
        char letraInicial2 = palavra2.charAt(0);
        char letraFinal2 = palavra2.charAt(tam2 - 1);

        if (letraInicial1 == letraInicial2 && letraFinal1 == letraFinal2) {
                System.out.println("S");
        } else {
                System.out.println("N");
        }
    }
}