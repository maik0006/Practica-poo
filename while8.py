class Tareas:
    #Maikol Daniel Torres Fandiño
    def __init__(self):
        self.lista = []

    def ejecutar(self):
        while True:
            tarea = input("Nueva tarea (o 'fin'): ")
            if tarea == "fin":
                break
            self.lista.append(tarea)
        print("Tareas guardadas:", self.lista)

t = Tareas()
t.ejecutar()

