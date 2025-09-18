class RegistroPersonas:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.personas = []  

    def agregar_persona(self, nombre, edad, ciudad):
        self.personas.append((nombre, edad, ciudad))

    def mostrar_personas(self):
        for nombre, edad, ciudad in self.personas:
            print(f"{nombre}, {edad} años, vive en {ciudad}")


r = RegistroPersonas()
r.agregar_persona("Carlos", 30, "Madrid")
r.agregar_persona("Lucía", 25, "Barcelona")
r.mostrar_personas()
