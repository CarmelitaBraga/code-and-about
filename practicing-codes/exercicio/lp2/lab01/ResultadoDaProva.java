/**
 * Laboratório de Programação 2 - Lab 01
 *
 * @author Carmelita Braga - 121210008
 */

import java.util.Scanner;

public class ResultadoDaProva {
        public static int[] dobraArray(int[] arrayOriginal) {
                int[] novoArray = new int[arrayOriginal.length * 2];
                for (int i = 0; i < arrayOriginal.length; i++) {
                        arrayOriginal[i] = novoArray[i];
                }

                return novoArray;
        }

        public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);

                int[] alunoNota = new int[100];
                int soma = 0;
                int contador = 0;
                while (true) {
                        String[] dados = sc.nextLine().split(" ");
                        if (dados[0].equals("-")) {
                                break;
                        }
                        alunoNota[contador] = Integer.parseInt(dados[1]);
                        if (contador == 100) {
                                dobraArray(alunoNota);
                        }
                        soma += alunoNota[contador];
                        contador += 1;
                        }
                int media = soma / contador;
                int maior = alunoNota[0];
                int menor = alunoNota[0];
                int abaixo = 0;
                int acima = 0;
                for (int i = 0; i < contador; i++) {
                        if (alunoNota[i] >= 700) {
                                acima += 1;
                        }
                        else if (alunoNota[i] < 700) {
				abaixo += 1;
                        }

                        if (alunoNota[i] > maior) {
                                maior = alunoNota[i];
                        }
                        if (alunoNota[i] < menor) {
                                menor = alunoNota[i];
                        }
                }

		System.out.println("maior: " + maior);
		System.out.println("menor: " + menor);
		System.out.println("media: " + media);
		System.out.println("acima: " + acima);
		System.out.println("abaixo: " + abaixo);
        }
}
