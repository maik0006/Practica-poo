class Cuadrados:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, n):
        self.n = n

    def generar(self):
        for i in range(1, self.n+1):
            print(f"{i}² = {i**2}")

c = Cuadrados(5)
c.generar()
