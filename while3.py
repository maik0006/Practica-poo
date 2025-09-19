class Juego:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, secreto):
        self.secreto = secreto

    def jugar(self):
        intento = None
        while intento != self.secreto:
            intento = int(input("Adivina el número: "))
        print("¡Correcto!")

juego = Juego(7)
juego.jugar()
