class Cajero:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Retiro exitoso. Saldo:", self.saldo)
        else:
            print("Saldo insuficiente")

cajero = Cajero(100)
while cajero.saldo > 0:
    monto = int(input("Ingrese monto a retirar (0 para salir): "))
    if monto == 0:
        break
    cajero.retirar(monto)
