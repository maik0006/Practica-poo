class Menu:
    #Maikoll Daniel Torres Fandiño
    def __init__(self):
        self.platos = {}  

    def agregar_plato(self, nombre, precio):
        self.platos[nombre] = precio

    def mostrar_menu(self):
        for plato, precio in self.platos.items():
            print(f"{plato}: ${precio:.2f}")

m = Menu()
m.agregar_plato("Pizza", 12.5)
m.agregar_plato("Ensalada", 8.0)
m.mostrar_menu()
