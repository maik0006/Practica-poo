class Contador:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1
        print("Contador:", self.valor)

contador = Contador()
while contador.valor < 5:
    contador.incrementar()
