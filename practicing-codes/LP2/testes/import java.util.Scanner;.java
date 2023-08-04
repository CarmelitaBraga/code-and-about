import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class ProcurandoWally {
        public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                ArrayList nomesIguais = new ArrayList();

                while (true) {
                        String[] nomes = sc.nextLine().split(" ");

                        if (nomes[0].equals("wally")) {
                                break;
                        }

                        boolean existencia = false;

                        for (int i = 0; i < nomes.length; i++) {
                                if (nomes[i].length == 5) {
                                        nomesIguais.add(nome);
                                        existencia = true;
                                }
                        }
                        if (existencia == false) {
                                nomesIguais.add("?");
                        }
                }
                for (int j = 0; j < nomesIguais.length; j++) {
                                System.out.println(nomesIguais[j]);
                }

        }
}