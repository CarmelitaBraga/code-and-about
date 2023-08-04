/**
 * Laboratório de Programação 2 - Lab 1
 *
 * @author Carmelita Braga de Araújo Medeiros - 121210008
 */

import java.util.Scanner;

/*public class CalculadoraComOpcao {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String oper = sc.next();
		float a = sc.nextFloat();
		float b = sc.nextFloat();

		if (oper.equals("*")) {
			System.out.println(a * b);
		} else if (oper.equals("/")) {
			if (b == 0) {
				System.out.println("ERRO");
			} else {
			System.out.println(a / b);
			}
		} else if (oper.equals("+")) {
			System.out.println(a + b);
		} else if (oper.equals("-")) {
			System.out.println(a - b);
		} else {
			System.out.println("ENTRADA INVALIDA");
		}

	}
}
*/

import java.util.Scanner;

public class CalculadoraComOpcao {
        public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                String oper = sc.next();

                if (oper.equals("*") || oper.equals("/") || oper.equals("+") || oper.equals("-")) {
                    float a = sc.nextFloat();
                    float b = sc.nextFloat();

                    if (oper.equals("*")) {
                            System.out.println("RESULTADO: " + (a * b));
                    } else if (oper.equals("/")) {
                            if (b == 0) {
                                    System.out.println("ERRO");
                            } else {
                            System.out.println("RESULTADO: " + (a / b));
                            }
                    } else if (oper.equals("+")) {
                            System.out.println("RESULTADO: " + (a + b));
                    } else if (oper.equals("-")) {
                            System.out.println("RESULTADO: " + (a- b));
        	        }
		}
	       	else {
                        System.out.println("ENTRADA INVALIDA");
                        }
                
        }
}

