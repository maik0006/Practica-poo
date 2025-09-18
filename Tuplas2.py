class HistorialAccesos:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.entradas = []  

    def registrar(self, usuario, hora):
        self.entradas.append((usuario, hora))

    def mostrar_historial(self):
        for usuario, hora in self.entradas:
            print(f"{usuario} accedió a las {hora}")

h = HistorialAccesos()
h.registrar("admin", "10:30")
h.registrar("jose", "11:00")
h.mostrar_historial()
