class ContaBancaria():
    def __init__(self,valor_inicial ):
        self.saldo = valor_inicial

    def sacar(self, valor):
        if valor > self.saldo :
            print("saldo insuficiente")
        else:
            #self.saldo = self.saldo - valor
            self.saldo -= valor
            print("Saque realizado com sucesso")

    def deposita(self, valor):
       self.saldo = self.saldo + valor
       print("Deposito realizado com secesso")

    def vericar_saldo(self):
        print(f"o saldo da conta é : {self.saldo}")

conta1 = ContaBancaria(1000)
conta1.deposita(500)
conta1.sacar(300)
conta1.vericar_saldo()