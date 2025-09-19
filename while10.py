class Juego:
    #Maikol Daniel Torres Fandiño
    def __init__(self, vidas):
        self.vidas = vidas

    def jugar(self):
        while self.vidas > 0:
            respuesta = input("Escribe 'ganar': ")
            if respuesta == "ganar":
                print("¡Ganaste!")
                return
            else:
                self.vidas -= 1
                print("Te quedan", self.vidas, "vidas")
        print("Game Over")

j = Juego(3)
j.jugar()
