class Puntajes:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.lista_puntajes = []  

    def agregar_puntaje(self, nombre, puntaje):
        self.lista_puntajes.append((nombre, puntaje))

    def mostrar_puntajes(self):
        print("Puntajes:")
        for nombre, puntos in self.lista_puntajes:
            print(f"{nombre}: {puntos} puntos")

juego = Puntajes()
juego.agregar_puntaje("Laura", 150)
juego.agregar_puntaje("Mario", 200)
juego.mostrar_puntajes()
