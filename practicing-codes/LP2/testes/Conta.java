public class Conta {
    private String cpf;
    public Conta(String cpf) {
        if (cpf == null) {
            throw new NullPointerException("CPF NULO");
        }
    }
}
