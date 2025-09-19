class Cuenta:
    #Maikol Daniel Torres Fandiño
    def __init__(self, saldo):
        self.saldo = saldo

    def menu(self):
        opcion = ""
        while opcion != "3":
            print("1) Depositar\n2) Retirar\n3) Salir")
            opcion = input("Elige: ")
            if opcion == "1":
                monto = int(input("Monto: "))
                self.saldo += monto
            elif opcion == "2":
                monto = int(input("Monto: "))
                if monto <= self.saldo:
                    self.saldo -= monto
                else:
                    print("Saldo insuficiente")
            print("Saldo actual:", self.saldo)

c = Cuenta(500)
c.menu()
