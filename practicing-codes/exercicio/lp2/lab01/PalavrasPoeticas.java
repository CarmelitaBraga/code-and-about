import java.util.*;

public class PalavrasPoeticas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String palavra1 = sc.next();
        int tam1 = palavra1.length();
        String letraInicial1 = palavra1.substring(0, 1);
        String letraFinal1 = palavra1.substring(tam1 - 1);

        String palavra2 = sc.next();
        int tam2 = palavra2.length();
        String letraInicial2 = palavra2.substring(0, 1);
        String letraFinal2 = palavra2.substring(tam2 - 1);

        if (letraInicial1.equals(letraInicial2) && letraFinal1.equals(letraFinal2)) {
                System.out.println("S");
        } else {
                System.out.println("N");
        }
    }
}
