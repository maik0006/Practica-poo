class Personas:
    def __init__(self, edad, nombre, genero):

        self.edad= edad
        self.nombre=nombre
        self.genero=genero


personas1= Personas(16,"Juan","Masculino")
print("-"*20)
print(personas1.edad, personas1.nombre, personas1.genero)



