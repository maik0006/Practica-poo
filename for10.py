class Lista:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, elementos):
        self.elementos = elementos

    def mostrar(self):
        for i, elem in enumerate(self.elementos):
            print(f"Posición {i}: {elem}")

l = Lista(["manzana", "pera", "uva"])
l.mostrar()
