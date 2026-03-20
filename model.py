class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente, saldo_inicial):
        self.cliente = cliente
        self.saldo = saldo_inicial

class BancoDados:
    # Simulação de banco de dados usando uma lista
    contas = []

    @classmethod
    def salvar_conta(cls, conta):
        cls.contas.append(conta)