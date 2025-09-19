class Intentos:
    #Maikol Daniel Torres Fandiño
    def __init__(self, limite):
        self.limite = limite

    def jugar(self):
        intentos = 0
        while intentos < self.limite:
            palabra = input("Escribe 'python': ")
            if palabra == "python":
                print("¡Bien hecho!")
                return
            intentos += 1
        print("Límite de intentos alcanzado")

juego = Intentos(3)
juego.jugar()
