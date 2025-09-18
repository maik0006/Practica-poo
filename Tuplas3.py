class ObjetoGrafico:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, nombre, ancho, alto):
        self.nombre = nombre
        self.dimensiones = (ancho, alto)

    def redimensionar(self, nuevo_ancho, nuevo_alto):
        self.dimensiones = (nuevo_ancho, nuevo_alto)

    def mostrar(self):
        print(f"{self.nombre} - Dimensiones: {self.dimensiones}")

obj = ObjetoGrafico("Ventana", 800, 600)
obj.mostrar()
obj.redimensionar(1024, 768)
obj.mostrar()
