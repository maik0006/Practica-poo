class alumno:
    def __init__(self,nombre,curso,grado):

        self.nombre=nombre
        self.curso=curso
        self.grado=grado

alumno1=alumno("Fabian","601","sexto")
print("-"*30)
print(alumno1.nombre, alumno1.curso, alumno1.grado)
        