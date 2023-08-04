/**
 * Laboratório de Programação 2
 *
 * @author Carmelita Braga
 */

import java.util.Scanner;
 
import java.util.*;
 
public class AlturaAviao {
   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int alturaIdeal = sc.nextInt();
       int alturaProx = sc.nextInt();
       int limAntigo = Math.abs(alturaIdeal - alturaProx);

       while (true) {
        alturaProx = sc.nextInt();
	if (alturaIdeal == alturaProx) {
            System.out.println("OK");
            break;
        }
        int lim = Math.abs(alturaIdeal - alturaProx);
 
        if (limAntigo <= lim ) {
            System.out.println("PERIGO");
        } else if (limAntigo > lim) {
            System.out.println("ADEQUADO");
        }
        limAntigo = lim;
       }
   }
}
