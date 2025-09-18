class ListaNumeros:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, numeros):
        self.numeros = numeros

    def mostrar(self):
        for numero in self.numeros:
            print(f"Número: {numero}")

lista = ListaNumeros([1, 2, 3, 4, 5])
lista.mostrar()
