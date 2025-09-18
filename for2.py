class SumaLista:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, numeros):
        self.numeros = numeros

    def sumar(self):
        total = 0
        for n in self.numeros:
            total += n
        print(f"Suma total: {total}")

s = SumaLista([3, 6, 9])
s.sumar()
