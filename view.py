from tkinter import messagebox, simpledialog


class BancoView:
    def obter_dados_conta(self):
        nome = simpledialog.askstring("Entrada", "Digite o Nome do Cliente:")
        cpf = simpledialog.askstring("Entrada", "Digite o CPF:")
        try:
            saldo = float(simpledialog.askstring("Entrada", "Digite o Saldo Inicial:"))
        except (TypeError, ValueError):
            saldo = 0.0

        return nome, cpf, saldo

    def exibir_conta(self, conta):
        mensagem = (f"--- Dados da Conta ---\n"
                    f"Cliente: {conta.cliente.nome}\n"
                    f"CPF: {conta.cliente.cpf}\n"
                    f"Saldo: R$ {conta.saldo:.2f}")
        messagebox.showinfo("Sucesso", mensagem)