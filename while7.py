class Temporizador:
    #Maikol Daniel Torres Fandiño
    def __init__(self, tiempo):
        self.tiempo = tiempo

    def iniciar(self):
        while self.tiempo > 0:
            print("Tiempo:", self.tiempo)
            self.tiempo -= 1
        print("¡Tiempo terminado!")

t = Temporizador(5)
t.iniciar()
