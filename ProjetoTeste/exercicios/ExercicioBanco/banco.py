import contas
import pessoas


class Banco:
    def __init__(self, agencias: list[int] | None = None,
                 clientes: list[pessoas.Pessoa] | None = None,
                 contas: list[contas.Conta] | None = None):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('checar_agencia', True)
            return True
        print('checar_agencia', False)
        return False

    def checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('checar_cliente', True)
            return True
        print('checar_cliente', False)
        return False
    def checa_conta(self, conta):
        if conta in self.contas:
            print('checar_conta', True)
            return True
        print('checar_conta', False)
        return False

    def conta_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('Conta do cliente', True)
            return True
        print('Conta do cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self.checa_agencia(conta) and \
            self.checa_cliente(cliente) and \
            self.checa_conta(conta) and \
            self.conta_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'

if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111,222,0,0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1,cp1])
    banco.agencias.extend([111, 222])
    print(banco.autenticar(c1, cc1))
    print(banco)

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        cc1.sacar(5)
        print(c1.conta)
