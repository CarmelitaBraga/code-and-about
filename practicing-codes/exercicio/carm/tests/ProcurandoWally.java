import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class ProcurandoWally {
        public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                //ArrayList<String> tamIgual = new ArrayList<String>();

                String[] tamIgual = new String[100];
                int cont = 0;
                while (true) {
                        String[] nomes = sc.nextLine().split(" ");

                        if (nomes[0].equals("wally")) {
                                break;
                        }

                        boolean existencia = false;
                        int tam = nomes.length;

                        for (int i = 0; i < tam; i++) {
                                if (nomes[i].length() == 5) {
                                        tamIgual[cont] = nomes[i];
                                        existencia = true;
                                        cont += 1;
                                }
                        }
                        if (existencia == false) {
                                tamIgual[cont] = "?";
                                cont += 1;
                        }
                }

                int tamF = tamIgual.length;
                for (int j = 0; j < tamF; j++) {
                                System.out.println(tamIgual[j]);
                }

        }
}

