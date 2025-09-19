class Cadena:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, texto):
        self.texto = texto

    def invertir(self):
        for letra in reversed(self.texto):
            print(letra, end=" ")
        print()

c = Cadena("Python")
c.invertir()
