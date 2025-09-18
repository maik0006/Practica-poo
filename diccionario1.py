class Votacion:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.votos = {}  

    def votar(self, opcion):
        self.votos[opcion] = self.votos.get(opcion, 0) + 1

    def mostrar_resultados(self):
        for opcion, cantidad in self.votos.items():
            print(f"{opcion}: {cantidad} votos")

v = Votacion()
v.votar("Opción A")
v.votar("Opción B")
v.votar("Opción A")
v.mostrar_resultados()
