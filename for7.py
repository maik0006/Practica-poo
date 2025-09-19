class Numeros:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, lista):
        self.lista = lista

    def pares(self):
        for n in self.lista:
            if n % 2 == 0:
                print(n, "es par")

nums = Numeros([1, 2, 3, 4, 5, 6])
nums.pares()
