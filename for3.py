class Buscador:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, numeros):
        self.numeros = numeros

    def buscar(self, objetivo):
        for n in self.numeros:
            if n == objetivo:
                print(f"{objetivo} encontrado.")
                return
        print(f"{objetivo} no está en la lista.")

b = Buscador([10, 20, 30])
b.buscar(20)
b.buscar(40)
