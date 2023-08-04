public class Mapa {
    public static void main(String[] args) {
        Ponto p1 = new Ponto(20, 10);
        Ponto p2 = new Ponto(30, -10);
        /**p1.x = 20;
        p1.y = 10;
        p2.x = 0;
        p2.y = -10;*/
        System.out.println(p1.distancia(p2));
    }
}