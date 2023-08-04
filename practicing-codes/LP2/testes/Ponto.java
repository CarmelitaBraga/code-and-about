public class Ponto {

    private int x;
    private int y;

    public Ponto(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public double distancia(Ponto p) { //método
        double xDist = this.x - p.x;
        double yDist = this.y - p.y;

        return Math.sqrt(xDist * xDist + yDist * yDist);
    }

}
