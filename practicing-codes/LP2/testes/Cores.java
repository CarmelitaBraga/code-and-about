import java.util.*;

public class Cores {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int red = sc.nextInt();
        int green = sc.nextInt();
        int blue = sc.nextInt();

        if (red < 128 || green < 128 || blue < 128) {
            System.out.println("PRETO");
        } else if (red > 128 && green > 128 && blue > 128) {
            System.out.println("BRANCO");
        }
    }
}
