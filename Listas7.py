class Libro:
    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor
    
class Biblioteca:
    def __init__(self):
        self.libros =[]

    def agregar_libro(self,Libro):
        self.libros.append(Libro)

biblioteca= Biblioteca()
biblioteca.agregar_libro(Libro("Moby dick","Herman Melveille"))
print(biblioteca.libros[0].titulo)