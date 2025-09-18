class Estudiante:
    #Maikoll Daniel Torres Fandiño
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {} 

    def agregar_nota(self, materia, nota):
        self.notas[materia] = nota

    def mostrar_notas(self):
        for materia, nota in self.notas.items():
            print(f"{materia}: {nota}")

e = Estudiante("Carlos")
e.agregar_nota("Matemáticas", 90)
e.agregar_nota("Historia", 85)
e.mostrar_notas()
