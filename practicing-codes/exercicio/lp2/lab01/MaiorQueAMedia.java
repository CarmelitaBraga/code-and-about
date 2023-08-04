/**
 * Laboratório de Programação 2 - Lab 1
 *
 * @author Carmelita Braga - 121210008
 */

import java.util.Scanner;
import java.util.Arrays;

public class MaiorQueAMedia {
        public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                String[] sNums = sc.nextLine().split(" ");
                int tam = sNums.length;

                int[] nums = new int[tam];
                double soma = 0;
                for (int i = 0; i < tam; i++) {
                        nums[i] = Integer.parseInt(sNums[i]);
                        soma += nums[i];

                }
                double media = (soma/tam);
                for (int j = 0; j < nums.length; j++) {
                        if (nums[j] > media) {
                                System.out.print(nums[j] + " ");
                        }
                }
                System.out.println();
        }
}

