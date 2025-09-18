class RegistroTemperaturas:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.registros = []  

    def agregar(self, dia, temperatura):
        self.registros.append((dia, temperatura))

    def mostrar(self):
        for dia, temp in self.registros:
            print(f"{dia}: {temp}°C")


registro = RegistroTemperaturas()
registro.agregar("Lunes", 22)
registro.agregar("Martes", 25)
registro.mostrar()
