class Calificaciones:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.notas = {} 

    def agregar_nota(self, nombre, nota):
        if nombre not in self.notas:
            self.notas[nombre] = []
        self.notas[nombre].append(nota)

    def mostrar_todo(self):
        for nombre, lista in self.notas.items():
            promedio = sum(lista) / len(lista)
            print(f"{nombre}: {lista} (Promedio: {promedio:.2f})")
            
c = Calificaciones()
c.agregar_nota("Juan", 8)
c.agregar_nota("Juan", 9)
c.agregar_nota("María", 10)
c.mostrar_todo()
