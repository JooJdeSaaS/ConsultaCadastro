import tkinter as tk
from model import Cliente, Conta, BancoDados
from view import BancoView


class BancoController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Esconde a janela principal do Tkinter
        self.view = BancoView()

    def criar_nova_conta(self):
        nome, cpf, saldo = self.view.obter_dados_conta()

        if nome and cpf:
            novo_cliente = Cliente(nome, cpf)
            nova_conta = Conta(novo_cliente, saldo)

            BancoDados.salvar_conta(nova_conta)

            self.view.exibir_conta(nova_conta)
        else:
            messagebox.showwarning("Erro", "Dados inválidos!")


if __name__ == "__main__":
    app = BancoController()
    app.criar_nova_conta()