class ContadorVocales:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, palabra):
        self.palabra = palabra

    def contar(self):
        vocales = "aeiou"
        total = 0
        for letra in self.palabra.lower():
            if letra in vocales:
                total += 1
        print(f"La palabra '{self.palabra}' tiene {total} vocales.")

cv = ContadorVocales("Programacion")
cv.contar()
