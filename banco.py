
class ContaBancaria():
    titular = ""
    saldo = 0.0
    limite = 0.0

    def __init__(self, titular: str, saldo: float, limite: float):
        self.titular = str(titular)
        self.saldo = float(saldo)
        self.limite = float(limite)

    def depositar(self, valor):
        if valor <= 0:
            print("0")
        else:
            self.saldo += valor
            print("1")
    
    def levantar(self, valor):
        if valor <= 0:
            print("0")
        elif (self.saldo + self.limite) - valor >= 0:
            self.saldo -= valor
            print("1")
        else:
            print("0")

    def exibir_saldo(self):
        print(f"{self.saldo:.2f}")
    
    def exibir_info(self):
        """[titular] [saldo] [limite]"""
        print("["+self.titular+"] ["+str(self.saldo)+"] ["+str(self.limite)+"]")


"""
conta = ContaBancaria("Cesar", "20", 10)
#conta.depositar(10)
#conta.levantar(21)
conta.exibir_info()
conta.exibir_saldo()
"""