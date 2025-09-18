
class Contador:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, elementos):
        self.elementos = elementos

    def contar(self):
        count = 0
        for _ in self.elementos:
            count += 1
        print(f"Número de elementos: {count}")

c = Contador(["a", "b", "c", "d","g","o","q"])
c.contar()
